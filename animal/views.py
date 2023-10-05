# Create your views here.
import datetime

from django.shortcuts import render

from animal.models import Animal, Schedule
from animal.time_scheduler import calculate_booking_time


def index(request):
    animals = Animal.objects.all()
    animal_type = request.GET.get("animal_type")
    animal_breed = request.GET.get("animal_breed")
    if animal_type:
        animals = animals.filter(type=animal_type)
    if animal_breed:
        animals = animals.filter(breed=animal_breed)
    types = []
    breeds = []
    for animal in animals:
        if animal.breed not in breeds:
            breeds.append(animal.breed)
        if animal.type not in types:
            types.append(animal.type)
    return render(request, template_name="animal/index.html",
                  context={"animals": animals, "types": types, "breeds": breeds})


def animal_detail(request, animal_id):
    time_duration = None
    free_time = []
    acceptable_time_for_booking = [1, 2, 3, 4]
    animal = Animal.objects.get(id=animal_id)
    is_time_duration_changed = False
    if request.method == "POST":
        if request.POST.get("time_duration"):
            request.session["time_duration"] = int(request.POST.get("time_duration"))
            time_duration = request.POST.get("time_duration")
            if request.session.get("time_duration") != int(time_duration):
                is_time_duration_changed = True

        animal_schedule = Schedule.objects.filter(animal=animal)
        schedule = []
        for n in animal_schedule:
            if datetime.datetime.utcnow().date().strftime("%Y-%m-%d") == datetime.datetime.strftime(
                    n.start_time, "%Y-%m-%d"):
                schedule.append((n.start_time, n.end_time))
        if time_duration:
            free_time = calculate_booking_time(booked_time_frames=schedule, min_time_duration=time_duration)
        if not is_time_duration_changed and request.POST.get("start_time") and request.POST.get(
                'hidden_field') == "book":
            end_time = datetime.datetime.strptime(request.POST.get("start_time"), "%H:%M") + datetime.timedelta(
                hours=int(request.session["time_duration"]))
            end_datetime = datetime.datetime.utcnow().replace(hour=end_time.hour, minute=end_time.minute, second=0,
                                                              microsecond=0)
            start_time = datetime.datetime.strptime(request.POST.get("start_time"), "%H:%M")
            start_datetime = datetime.datetime.utcnow().replace(hour=start_time.hour, minute=start_time.minute,
                                                                second=0, microsecond=0)
            Schedule.objects.create(start_time=start_datetime,
                                    end_time=end_datetime,
                                    animal=animal,
                                    user=request.user)
            free_time = []
        return render(request, template_name="animal/animal_detail.html",
                      context={"animal": animal, "free_times": free_time, "time_fr": acceptable_time_for_booking,
                               "time_duration": request.session.get("time_duration")})
    else:
        return render(request, template_name="animal/animal_detail.html",
                      context={"animal": animal, "time_fr": acceptable_time_for_booking,
                               "time_duration": acceptable_time_for_booking[0]})

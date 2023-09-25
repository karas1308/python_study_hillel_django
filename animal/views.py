# Create your views here.
import datetime

from django.shortcuts import render

from animal.models import Animal
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
    acceptable_time_for_booking = [1, 2, 3, 4]
    animal = Animal.objects.get(id=animal_id)
    if request.method == "POST":
        time_duration = int(request.POST.get("time_duration", 3))
        # schedule = Schedule.objects.filter(animal=animal) # need date in db
        schedule = [(datetime.datetime(2023, 8, 1, 8, 0),
                     datetime.datetime(2023, 8, 1, 9, 0)),
                    (datetime.datetime(2023, 8, 1, 12, 30),
                     datetime.datetime(2023, 8, 1, 13, 0)),
                    (datetime.datetime(2023, 8, 1, 14, 30),
                     datetime.datetime(2023, 8, 1, 15, 0))]
        free_time = calculate_booking_time(booked_time_frames=schedule, min_time_duration=time_duration)
        return render(request, template_name="animal/animal_detail.html",
                      context={"animal": animal, "free_times": free_time, "time_fr": acceptable_time_for_booking})
    else:
        return render(request, template_name="animal/animal_detail.html",
                      context={"animal": animal, "time_fr": acceptable_time_for_booking})

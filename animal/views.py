# Create your views here.

from django.shortcuts import render

from animal.models import Animal


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
    return render(request, template_name="animal/index.html", context={"animals": animals, "types": types, "breeds": breeds})

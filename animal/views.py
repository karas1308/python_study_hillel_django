# Create your views here.
import operator

from django.db.models import Q
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
    return render(request, template_name="animal/index.html", context={"animals": animals})

# Create your views here.
from django.shortcuts import render


def index(request):
    return render(request, template_name="animal/index.html")

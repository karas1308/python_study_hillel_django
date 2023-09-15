# Create your views here.
from django.shortcuts import render


def index(request):
    return render(request, template_name="user/index.html")


def user_login(request):
    return render(request, template_name="user/index.html")


def user_logout(request):
    return render(request, template_name="user/index.html")


def user_register(request):
    return render(request, template_name="user/index.html")


def user_history(request):
    return render(request, template_name="user/index.html")

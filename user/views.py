# Create your views here.
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseNotFound, JsonResponse
from django.shortcuts import redirect, render


def index(request):
    return render(request, template_name="user/index.html")


def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(
            request,
            username=username,
            password=password
        )
        if user is not None:
            login(request, user)
            response_text = "ok"
            return HttpResponse(response_text)
        else:
            response_text = "fail"
            return HttpResponseNotFound(response_text)
    if request.user.is_authenticated:
        return redirect("/")
    return render(request, template_name="user/login.html")


def user_logout(request):
    logout(request)
    return redirect("/login")


def user_register(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        email = request.POST.get("email")
        user = User.objects.create_user(username=username,
                                        password=password,
                                        email=email)
        if user.username == username:
            return JsonResponse({"username": user.username, "is_superuser": user.is_superuser}, safe=False)
        else:
            response_text = "fail"
            return HttpResponseNotFound(response_text)
    return render(request, template_name="user/register.html")


def user_history(request):
    return render(request, template_name="user/index.html")

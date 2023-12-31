from django.urls import path

from user import views

urlpatterns = [
    # path('user/', views.index, name="index"),
    path('', views.index, name="index"),
    path('login/', views.user_login, name="user_login"),
    path('logout/', views.user_logout, name="user_logout"),
    path('register/', views.user_register, name="user_register"),
    path('user/history/', views.user_history, name="user_history"),
]

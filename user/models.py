from django.contrib.auth.models import User
from django.db import models


# Create your models here.

# class User(models.Model):
#     name = models.CharField(max_length=255)
#     password = models.CharField(max_length=255)
#     login = models.CharField(max_length=30)
#     phone = models.CharField(max_length=15)
#
#     def __str__(self):
#         return self.name


class UserMedia(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    media_link = models.CharField(max_length=255)

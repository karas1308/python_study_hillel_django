from django.db import models


# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    login = models.CharField(max_length=30)
    phone = models.CharField(max_length=15)
    media = models.CharField(max_length=255)

    def __str__(self):
        return self.name

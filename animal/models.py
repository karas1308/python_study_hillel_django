from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Animal(models.Model):
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    sex = models.ForeignKey('Sex', on_delete=models.CASCADE)
    age = models.PositiveIntegerField()
    breed = models.CharField(max_length=255)
    availability = models.BooleanField()
    description = models.TextField()
    healthy = models.BooleanField()

    def __str__(self):
        return f"{self.type} - {self.name}"


class AnimalMedia(models.Model):
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    media_link = models.CharField(max_length=255)
    main = models.BooleanField()

    def __str__(self):
        return self.media_link


class Sex(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Schedule(models.Model):
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.start_time} - {self.end_time}"

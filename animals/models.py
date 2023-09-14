from django.db import models


# Create your models here.

class Animals(models.Model):
    type = models.CharField(max_length=255)
    sex = models.ForeignKey('Sex', on_delete=models.CASCADE)
    age = models.PositiveIntegerField()
    breed = models.CharField(max_length=255)
    availability = models.BooleanField()
    description = models.TextField()
    healthy = models.BooleanField()


class AnimalMedia(models.Model):
    animal = models.ForeignKey(Animals, on_delete=models.CASCADE)
    media_link = models.CharField(max_length=255)  # edit
    main = models.BooleanField()


class Sex(models.Model):
    name = models.CharField(max_length=255)


class Schedule(models.Model):
    id = models.AutoField(primary_key=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    animal = models.ForeignKey(Animals, on_delete=models.CASCADE)
    # user = models.ForeignKey('user.customuser', on_delete=models.CASCADE)
import datetime

from django.contrib.auth.models import User
from django.db import models

from animal.models import Animal


# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Blog(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Feedback(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    media = models.ImageField(upload_to='images/', null=True, blank=True)
    date = models.DateField(default=datetime.datetime.date(datetime.datetime.utcnow()))
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

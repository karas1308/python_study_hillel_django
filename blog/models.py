from django.db import models

from animals.models import Animals
from user.models import User


# Create your models here.

class Tag(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Blog(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    text = models.TextField()
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Feedback(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    media = models.CharField(max_length=255)
    user = models.CharField(max_length=255)
    date = models.ForeignKey(User, on_delete=models.CASCADE)
    animal = models.ForeignKey(Animals, on_delete=models.CASCADE)

    user_id = models.ForeignKey('user.customuser', on_delete=models.CASCADE)
    animal_id = models.ForeignKey('animal.animal', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title

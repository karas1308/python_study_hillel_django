from django import forms

from .models import Animal


class AnimalForm(forms.ModelForm):
    class Meta:
        model = Animal
        fields = "__all__"

# class Animal(models.Model):
#     name = models.CharField(max_length=255)
#     type = models.CharField(max_length=255)
#     sex = models.ForeignKey('Sex', on_delete=models.CASCADE)
#     age = models.PositiveIntegerField()
#     breed = models.CharField(max_length=255)
#     availability = models.BooleanField()
#     description = models.TextField()
#     healthy = models.BooleanField()
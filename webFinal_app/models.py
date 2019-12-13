from django.db import models
from django.urls import reverse


class Feedback(models.Model):
    name_of_user = models.CharField(max_length=10)
    email_of_user = models.EmailField(max_length=50)
    message_of_user = models.TextField()

    def __str__(self):
        return self.message_of_user


class Car(models.Model):
    model_of_car = models.CharField(max_length=100)
    about_car = models.TextField(default="foobar")

    def get_absolute_url(self):
        return reverse("car", kwargs={"id": self.id})

    def __str__(self):
        return self.model_of_car


class Characteristics(models.Model):
    cars = models.ForeignKey(Car, on_delete='CASCADE')
    volume_of_car = models.IntegerField()
    type_of_drive = models.CharField(max_length=200)
    transmission = models.CharField(max_length=50)
    carcase = models.CharField(max_length=100)

    def __str__(self):
        return self.carcase

from django.db import models

from django.contrib.auth.models import AbstractUser
from django.db import models



class Car(models.Model):
    model = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    Seats = models.IntegerField()
    Price = models.IntegerField()
    image = models.ImageField(upload_to='car_images/', null=True, blank=True)

    def __str__(self):
        return self.model

from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    # Add any additional fields you want in your custom user model
    email = models.EmailField(unique=True, null=False, blank=False)
    registration_method = models.CharField(
        max_length=10,
        choices=[
            ('email', 'Email'),
            ('google', 'Google'),
        ],
        default='email'
    )
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)


    def __str__(self):
        return self.email


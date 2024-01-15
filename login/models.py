from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class Userprofile(AbstractUser):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    place = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.username


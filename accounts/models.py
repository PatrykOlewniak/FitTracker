from django.db import models
from django.contrib.auth.models import AbstractUser


class AppUser(AbstractUser):
    height = models.FloatField(null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)

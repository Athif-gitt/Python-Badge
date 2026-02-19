from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    date_of_birth = models.DateField()
    address = models. CharField(max_length=100, blank=True)
    bio_info = models.TextField(max_length=500)

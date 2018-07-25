from django.db import models
from django.contrib.auth.models import AbstractUser



class CustomUser(AbstractUser):

    name = models.CharField(blank=True, max_length=225)

    def __str__(self):
        return self.email

# Create your models here.

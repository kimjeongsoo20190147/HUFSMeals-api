from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    username = models.CharField(null=True, unique=False, max_length=20)
    google_id = models.CharField(max_length=30, unique=True, null = True)
    nickname = models.CharField(max_length=100, null = True)
    country = models.CharField(max_length=10)

    USERNAME_FIELD = 'google_id'

    def __str__(self):
        return self.nickname
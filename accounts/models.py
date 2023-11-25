from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    google_id = models.BigIntegerField(unique=True, null = True)
    nickname = models.CharField(max_length=100, null = True)
    country = models.CharField(max_length=10)

    def __str__(self):
        return self.nickname
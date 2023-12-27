from django.db import models

# Create your models here.
class Restaurant(models.Model):
    name = models.CharField(max_length = 50)
    latitude = models.FloatField(default = 0.0)
    longitude = models.FloatField(default = 0.0)
    opening_hours = models.TextField(default = "")
    address = models.CharField(max_length = 200)
    category = models.CharField(max_length = 50)
    phone = models.CharField(max_length = 50)
    review_cnt = models.IntegerField(default = 0)
    score_avg = models.FloatField(default = 0)
from django.db import models

# Create your models here.
def restaurant_images_path(instance, filename):
    return f'restaurant_images'

class Restaurant(models.Model):
    name = models.CharField(max_length = 50)
    restaurant_image = models.ImageField(upload_to = restaurant_images_path, blank = True, null = True)
    latitude = models.CharField(max_length = 20)
    longitude = models.CharField(max_length = 20)
    opening_hours = models.TextField(default = "")
    address = models.CharField(max_length = 200)
    category = models.CharField(max_length = 50)
    phone = models.CharField(max_length = 50)
    review_cnt = models.IntegerField(default = 0)
    score_avg = models.FloatField(default = 0)


def menu_images_path(instance, filename):
    return f'menu_images/{instance.restaurant.name}_{instance.restaurant.pk}'

class Menu(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete = models.CASCADE)
    name = models.CharField(max_length = 50)
    menu_image = models.ImageField(upload_to = menu_images_path, blank = True, null = True)
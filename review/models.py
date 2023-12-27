from django.db import models
from accounts.models import User
from restaurant.models import Restaurant

def user_images_path(instance, filename):
    return f'user_images/{instance.user.pk}'

class Review(models.Model):
    user = models.ForeignKey(User, null = True, on_delete = models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, null = True, on_delete = models.CASCADE)
    rate = models.IntegerField(default= 0)
    image = models.ImageField(upload_to = user_images_path, blank = True, null = False)
    title = models.CharField(max_length = 100)
    body = models.TextField(default = "")

    def __str__(self):
        return self.title
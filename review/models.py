from django.db import models
from accounts.models import User
from restaurant.models import Restaurant

def user_images_path(instance, filename):
    return f'user_images/{instance.user.pk}'

class Review(models.Model):
    user = models.ForeignKey(User, null = True, on_delete = models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, null = True, on_delete = models.CASCADE)
    title = models.CharField(max_length = 100)
    body = models.TextField(default = "")
    src_lang = models.CharField(max_length = 10, null = True)
    created_at = models.DateField(auto_now_add = True, null = True)
    score = models.IntegerField(default= 0)
    
    def __str__(self):
        return self.title
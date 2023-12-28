from django.db import models
from accounts.models import User
from restaurant.models import Restaurant

def review_photo_path(instance, filename):
    return f'review_photo/{instance.review.pk}'

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
    

class ReviewPhoto(models.Model):
    review = models.ForeignKey(Review, on_delete = models.CASCADE)
    photo = models.ImageField(upload_to = review_photo_path, blank = True)
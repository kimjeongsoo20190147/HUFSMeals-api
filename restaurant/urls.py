from django.urls import path
from restaurant.views import *

app_name = 'restaurant'

urlpatterns = [
    path('create/', RestaurantRegisterView.as_view()),
]
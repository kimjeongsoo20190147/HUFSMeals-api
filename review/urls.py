from django.urls import path
from review.views import *

app_name = 'review'

urlpatterns = [
    path('', ReviewView.as_view()),
    path('create/', ReviewCreate.as_view()),
    path('update/<int:pk>/', ReviewUpdate.as_view()),
    path('delete/<int:pk>', ReviewDelete.as_view()),
]
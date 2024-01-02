from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework import status
from ..serializers import *
from ..models import *
from django.db.models import Q
import json

class RestaurantRegisterView(CreateAPIView):
    """
    식당 등록 view
    """
    serializer_class = CreateRestaurantSerializer
    queryset = Restaurant.objects.all()
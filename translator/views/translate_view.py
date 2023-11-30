from django.shortcuts import render
from rest_framework.decorators import api_view
import requests
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.views import APIView
import json

client_id = "cGwhwDRITcSEobTG98HL"
secret = "mNrbhhkyEC"

class Translatre(APIView):
    """
    파파고 번역 api view
    """
    authentication_classes = [JWTAuthentication]
    def post(self, request):
        text = request.data['text']
        source = request.data['source']
        translate_api = "https://openapi.naver.com/v1/papago/n2mt"
        headers = {
            'X-Naver-Client-Id' : client_id,
            'X-Naver-Client-Secret' : secret
        }
        data = {
            "source" : source,
            "target" : self.request.user.country,
            "text" : text
        }
        response = requests.post(translate_api, headers=headers, data=data).json()
        return Response(response)
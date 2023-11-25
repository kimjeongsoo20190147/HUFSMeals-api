from rest_framework.views import APIView
import requests
from django.shortcuts import redirect
from django.conf import settings
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.core.exceptions import ValidationError
GOOGLE_ACCESS_TOKEN_OBTAIN_URL = 'https://oauth2.googleapis.com/token'
GOOGLE_USER_INFO_URL = 'https://www.googleapis.com/oauth2/v3/userinfo'


class GoogleLoginApi(APIView):
    def get(self, request):
        app_key = "694730838559-u7slukjsulo3h4r0qhjln4ah8lnjmftt.apps.googleusercontent.com"
        scope = "https://www.googleapis.com/auth/userinfo.email " + \
                "https://www.googleapis.com/auth/userinfo.profile"
        
        redirect_uri = "http://127.0.0.1:8000/accounts/login/"
        google_auth_api = "https://accounts.google.com/o/oauth2/v2/auth"

        response = redirect(
            f"{google_auth_api}?client_id={app_key}&response_type=code&redirect_uri={redirect_uri}&scope={scope}"
        )
        
        return response


class GoogleLogin(APIView):
    def google_login(self, request):
        code = request.GET.get('code')
        token_url = "https://oauth2.googleapis.com/token"
        data = {
            "client_id" : "694730838559-u7slukjsulo3h4r0qhjln4ah8lnjmftt.apps.googleusercontent.com",
            "client_secret" : "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",
            "code" : code,
            "grant_type" : 'authorization_code',
            "redirect_uri" : "http://127.0.0.1:8000/accounts/login/"
        }
        
        access_token = requests.post(token_url, data=data).json().get('access_token')

        user_info_url = "https://www.googleapis.com/oauth2/v2/userinfo"
        user_information = requests.get(user_info_url, headers={"Authorization": f"Bearer {access_token}"}).json()

        return Response(user_information)
    
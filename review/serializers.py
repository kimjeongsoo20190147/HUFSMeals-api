from rest_framework import serializers
from .models import *

class CreateReviewSerializer(serializers.ModelSerializer):
    """
    리뷰 생성 시리얼라이저
    """
    class Meta:
        model = Review
        exclude = ['user', 'restaurant', 'src_lang']


class ReviewInfoSerializer(serializers.ModelSerializer):
    """
    리뷰 정보 시리얼라이저
    """
    class Meta:
        model = Review
        fields = '__all__'


class CreateReviewPhotoSerializer(serializers.ModelSerializer):
    """
    리뷰 사진 생성 시리얼라이저
    """
    class Meta:
        model = ReviewImage
        fields = ['photo']


class ReviewImageSerializer(serializers.ModelSerializer):
    """
    리뷰 사진 정보 시리얼라이저
    """
    class Meta:
        model = ReviewImage
        fields = '__all__'
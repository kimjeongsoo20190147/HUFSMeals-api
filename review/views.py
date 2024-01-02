from django.shortcuts import render
from .models import Review
from .serializers import CreateReviewSerializer
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny
from .permissions import IsOwnerOrReadOnly
from rest_framework.generics import ListCreateAPIView, UpdateAPIView, DestroyAPIView, CreateAPIView, ListAPIView


# class ReviewCreate(ListCreateAPIView):
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer
#     authentication_classes = [SessionAuthentication, BasicAuthentication]
#     permission_classes = [IsAuthenticatedOrReadOnly]
#     # permission_classes = [AllowAny]

#     def perform_create(self, serializer):
#         user = self.request.user
#         serializer.save(user=user)


# class ReviewUpdate(UpdateAPIView):
#     queryset = Review.objects.all()
#     serializer_class = 
#     authentication_classes = [SessionAuthentication, BasicAuthentication]
#     permission_classes = [IsOwnerOrReadOnly]


# class ReviewDelete(DestroyAPIView):
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer
#     authentication_classes = [SessionAuthentication, BasicAuthentication]
#     permission_classes = [IsOwnerOrReadOnly]



# # 예시: views.py
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework.permissions import IsAuthenticated

# class ReviewView(ListAPIView):
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer
#     authentication_classes = [SessionAuthentication, BasicAuthentication]
#     permission_classes = [IsAuthenticatedOrReadOnly]


# class ReviewCreate(ListCreateAPIView):
#     # permission_classes = [IsAuthenticated]
#     permission_classes = [IsAuthenticatedOrReadOnly]
#     authentication_classes = [BasicAuthentication, SessionAuthentication]
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer
#     # permission_classes = [AllowAny]

#     def perform_create(self, serializer):
#         user = self.request.user
#         serializer.save(user = user)

#     def create(self, request, *args, **kwargs):
#         # POST 요청으로부터 게시글 데이터 추출
#         data = request.data

#         # 게시글 생성 및 저장
#         review = Review(user=request.user, title=data['title'], body=data['body'], rate=data['rate'])
#         review.save()

#         # 시리얼라이저를 사용하여 응답 데이터 생성
#         serializer = ReviewSerializer(review)
#         return Response(serializer.data, status=201)

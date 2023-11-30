from django.shortcuts import render
from .models import Review
from .serializers import ReviewSerializer
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .permissions import IsOwnerOrReadOnly
from rest_framework.generics import ListCreateAPIView, UpdateAPIView, DestroyAPIView


class ReviewCreate(ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(user=user)


class ReviewUpdate(UpdateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsOwnerOrReadOnly]


class ReviewDelete(DestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsOwnerOrReadOnly]
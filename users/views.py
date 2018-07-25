from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response

from rest_framework.views import APIView
from rest_framework import authentication, permissions

from users.serializers import UserSerializer
from . import models
from . import serializers


class UserListView(generics.ListCreateAPIView):
    queryset = models.CustomUser.objects.all()
    serializer_class = serializers.UserSerializer

# Create your views here.


class ListView(APIView):
    authentication_classes =(authentication.TokenAuthentication,)
    permission_classes =(permissions.IsAdminUser,)

    def get(self,request):
        usernames = [user.username for user in User.objects.all()]
        return Response(usernames)


class UserCreate(APIView):
    """
    Creates the user.
    """

    def post(self, request, format='json'):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                return Response(serializer.data,status=status.HTTP_201_CREATED)

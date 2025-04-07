#django
from django.shortcuts import render
from rest_framework import viewsets, generics, status


#local
from ..models import User
from ..serializers import UserSerializer



class RegistrationView(generics.CreateAPIView):
    queryset =  User.objects.all()
    serializer_class = UserSerializer

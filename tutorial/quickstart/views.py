from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User,Group
from rest_framework import viewsets
from rest_framework import permissions
from tutorial.quickstart.serializers import UserSerializers,GroupSerializer

class LoadPicViewset(viewsets.ModelViewSet):
    
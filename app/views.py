from django.shortcuts import redirect,render 
from .models import Neighbourhood, CustomUser , Profile ,Business, Post 
from rest_framework import generics, viewsets
from . import models
from . import serializers
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializers import UserSerializer, NeighbourhoodSerializer, ProfileSerializer
from .permissions import IsAdminOrReadOnly


# Create your views here.
def welcome(request):
    return render(request, 'welcome.html')

class UserSerializer(viewsets.ModelViewSet):
    queryset = models.CustomUser.objects.all()
    serializer_class = serializers.UserSerializer    

class NeighbourhoodSerializer(viewsets.ModelViewSet):
    queryset = Neighbourhood.objects.all()
    serializer_class = serializers.NeighbourhoodSerializer    
    permission_classes = [IsAdminOrReadOnly]

class ProfileSerializer(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = serializers.ProfileSerializer    

class BusinessSerializer(viewsets.ModelViewSet):
    queryset = Business.objects.all()
    serializer_class = serializers.BusinessSerializer
    permission_classes = [IsAdminOrReadOnly]

class PostSerializer(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = serializers.PostSerializer    
    permission_classes = [IsAdminOrReadOnly]

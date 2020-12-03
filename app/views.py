# from django.shortcuts import redirect,render, get_object_or_404
# from django.http import HttpResponseRedirect
# from django.contrib.auth import login, authenticate
# from .forms import  BusinessForm, NeighbourHoodForm, PostForm
# from django.contrib.auth.decorators import login_required
from .models import Neighbourhood, CustomUser  #Business, Post , 
from rest_framework import generics, viewsets
from . import models
from . import serializers
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializers import UserSerializer, NeighbourhoodSerializer
from .permissions import IsAdminOrReadOnly
from rest_framework.permissions import BasePermission, IsAdminUser, SAFE_METHODS


# Create your views here.
def welcome(request):
    return render(request, 'welcome.html')

class UserListView(generics.ListAPIView):
    queryset = models.CustomUser.objects.all()
    serializer_class = serializers.UserSerializer    

class NeighbourhoodSerializer(viewsets.ModelViewSet):
    queryset = Neighbourhood.objects.all()
    serializer_class = serializers.NeighbourhoodSerializer    
    permission_classes = (IsAdminOrReadOnly,)

# @login_required(login_url='login')
# def index(request):
#     return render(request, 'index.html')


# def create_neighbourhood(request):
#     if request.method == 'POST':
#         form = NeighbourHoodForm(request.POST, request.FILES)
#         if form.is_valid():
#             hood = form.save(commit=False)
#             hood.admin = request.user.profile
#             hood.save()
#             return redirect('hood')
#     else:
#         form = NeighbourHoodForm()
#     return render(request, 'newhood.html', {'form': form})

# def neighbourhoods(request):
#     all_hoods = Neighbourhood.objects.all()
#     all_hoods = all_hoods[::-1]
#     params = {
#         'all_hoods': all_hoods,
#     }
#     return render(request, 'neighbourhoods.html', params)

# def create_post(request, hood_id):
#     hood = Neighbourhood.objects.get(id=hood_id)
#     if request.method == 'POST':
#         form = PostForm(request.POST)
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.hood = hood
#             post.user = request.user.profile
#             post.save()
#             return redirect('single-hood', hood.id)
#     else:
#         form = PostForm()
#     return render(request, 'post.html', {'form': form})



# class UserList(APIView):
#     def get(self, request, format=None):
#         all_users = User.objects.all()
#         serializers = UserSerializer(all_users, many=True)
#         return Response(serializers.data)

#     def post(self, request, format=None):
#         serializers = UserSerializer(data=request.data)
#         if serializers.is_valid():
#             serializers.save()
#             return Response(serializers.data, status=status.HTTP_201_CREATED)
#         return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)    

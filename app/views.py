from django.shortcuts import render
# from rest_framework.response import Response
# from rest_framework.views import APIView
# from .serializers import UserSerializer
# from django.contrib.auth.models import User
# from rest_framework import status
from rest_framework import generics
from . import models
from . import serializers

# Create your views here.
def welcome(request):
    return render(request, 'welcome.html')


class UserListView(generics.ListAPIView):
    queryset = models.CustomUser.objects.all()
    serializer_class = serializers.UserSerializer    

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
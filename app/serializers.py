from rest_framework import serializers
from . import models

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CustomUser
        fields = ('email', 'username' )

class NeighbourhoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Neighbourhood
        fields = ('id','name', 'location', 'admin', 'description', 'healthcenter_number', 'police_number' )     
        
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Profile
        fields = ('__all__' )        
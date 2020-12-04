from rest_framework import serializers
from . import models
from .models import Profile
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CustomUser
        fields = ('email', 'username' )

# class ProfileSerializer(serializers.ModelSerializer):
#     """
#     A Profile serializer to return the Profile details
#     """
#     user = UserSerializer(required=True)

#     class Meta:
#         model = Profile
#         fields = ('profile_pic','name', 'bio', 'neighbourhood', 'email_address', 'location')

#     def create(self, validated_data):
#         """
#         Overriding the default create method of the Model serializer.
#         :param validated_data: data containing all the details of Profile
#         :return: returns a successfully created Profile record
#         """
#         user_data = validated_data.pop('user')
#         user = UserSerializer.create(UserSerializer(), validated_data=user_data)
#         profile, created = Profile.objects.update_or_create(user=user,
#                         profile_pic=validated_data.pop('profile_pic'), name=validated_data.pop('name'), bio=validated_data.pop('bio'), neighbourhood=validated_data.pop('neighbourhood'), email_address=validated_data.pop('email_address'),location=validated_data.pop('location'))
#         return profile        

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Profile
        fields = ('__all__' )  

class NeighbourhoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Neighbourhood
        fields = ('id','name', 'location', 'admin', 'description', 'healthcenter_number', 'police_number' )     
        
class BusinessSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Business
        fields = ('__all__' )        

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Post
        fields = ('__all__' )               
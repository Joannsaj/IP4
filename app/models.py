from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
# class Profile(models.Model):
#     profile = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
#     name = models.CharField(max_length=60)
#     location = models.CharField(max_length=60)
#     neighborhood = models.ForeignKey(Neighborhood, on_delete=models.CASCADE, related_name='neighbourhood')
#     profile_pic = CloudinaryField('image', null=True)
#     bio = models.TextField(null=True)
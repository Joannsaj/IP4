from django.db import models
import datetime as dt
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class User(AbstractUser):
    pass

class Profile(models.Model):
    profile = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    name = models.CharField(max_length=60)
    location = models.CharField(max_length=60)
    # neighborhood = models.ForeignKey(Neighborhood, on_delete=models.CASCADE, related_name='neighbourhood')
    profile_pic = CloudinaryField('image', null=True)
    bio = models.TextField(null=True)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()    

class Neighbourhood(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=60)
    admin = models.ForeignKey("Profile", on_delete=models.CASCADE, related_name='hood')
    neighbourhood_logo = models.ImageField(upload_to='images/')
    description = models.TextField()
    healthcenter_number = models.IntegerField(null=True, blank=True)
    police_number = models.IntegerField(null=True, blank=True)
    occupants_count = models.IntegerField(null=True, blank=True)


    def __str__(self):
        return f'{self.name} hood'

    def save_neighborhood(self):
        self.save()

    def delete_neighborhood(self):
        self.delete()

    @classmethod
    def find_neighborhood(cls, neighborhood_id):
        return cls.objects.filter(id=neighborhood_id)

class Business(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField(max_length=254)
    description = models.TextField(blank=True)
    neighbourhood = models.ForeignKey('Neighbourhood', on_delete=models.CASCADE, related_name='business')
    user = models.ForeignKey('Profile', on_delete=models.CASCADE, related_name='owner')

    def __str__(self):
        return f'{self.name} Business'

    def save_business(self):
        self.save()

    def delete_business(self):
        self.delete()

class Post(models.Model):
    title = models.CharField(max_length=120, null=True)
    post = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey('Profile', on_delete=models.CASCADE, related_name='post_owner')
    hood = models.ForeignKey('Neighbourhood', on_delete=models.CASCADE, related_name='hood_post')


    def __str__(self):
        return f'{self.title} Post'

    def save_post(self):
        self.save()

    def delete_post(self):
        self.delete()
            

# Generated by Django 3.1.4 on 2020-12-04 03:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_remove_profile_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='location',
            field=models.CharField(max_length=60, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='profile',
            name='name',
            field=models.CharField(max_length=60, null=True),
        ),
    ]

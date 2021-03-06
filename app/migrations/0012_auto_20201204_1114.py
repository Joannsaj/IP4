# Generated by Django 3.1.4 on 2020-12-04 11:14

import cloudinary.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_delete_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='income',
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_pic', cloudinary.models.CloudinaryField(max_length=255, null=True, verbose_name='image')),
                ('name', models.CharField(max_length=60, null=True)),
                ('bio', models.TextField(null=True)),
                ('email_address', models.EmailField(max_length=60)),
                ('location', models.CharField(max_length=60, null=True)),
                ('neighborhood', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='neighbourhood', to='app.neighbourhood')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

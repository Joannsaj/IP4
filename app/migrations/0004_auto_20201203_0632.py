# Generated by Django 3.1.4 on 2020-12-03 06:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20201203_0412'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='bio',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='location',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='profile_pic',
        ),
    ]
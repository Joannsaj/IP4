# Generated by Django 3.1.4 on 2020-12-04 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_business_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='income',
            field=models.TextField(max_length=200, null=True),
        ),
    ]

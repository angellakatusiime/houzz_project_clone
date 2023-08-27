from django.db import models

# Create your models here.


class MyModel(models.Model):
    imgname = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/', height_field=None, width_field=None, max_length=100)


class UserProfile(models.Model):
    # username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128) 

from django.db import models


# Create your models here.
class Customer(models.Model):

   Email = models.CharField(max_length=70)
   password = models.CharField(max_length=100)

def __str__(self):
     return self.Email

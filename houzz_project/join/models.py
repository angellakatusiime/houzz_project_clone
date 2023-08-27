from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    def __str__(self):
        return self.email
    
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='our_user'
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='our_user'
    )
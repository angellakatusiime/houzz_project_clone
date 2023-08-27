from django.contrib import admin
from .models import MyModel
from .models import UserProfile

# Register your models here.
# admin.py

admin.site.register(MyModel)
admin.site.register(UserProfile)

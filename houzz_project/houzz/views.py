from django.shortcuts import render
from .models import MyModel
from .models import UserProfile


# Create your views here.
def index(request):
    context ={
        'images' : MyModel.objects.all()
    }
    return render(request, 'index.html', context)






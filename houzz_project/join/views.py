from django.shortcuts import redirect, render
from django.urls import reverse
from .models import User
from django.http import HttpResponse
from django.contrib.auth import hashers
# Create your views here.
# sale view
def join_view(request):
    if request.method == 'GET':
        reg_email = request.GET.get('join_using_email')

        return render(request, 'join.html', {'reg_email': reg_email})
    return render(request, 'join.html')
        

def register_view(request):
    if request.method =='POST':
        useremail = request.POST.get('email')
        userpassword = request.POST.get('password')

        hashed_password = hashers.make_password(userpassword)
        new_user = User(
            email=useremail,
            username= useremail,
            password=hashed_password
        )
        new_user.save()
        return redirect(reverse('cart'))
    else:
        return redirect('not successfully registered')






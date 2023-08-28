from django.shortcuts import redirect, render
from django.urls import reverse
from .models import Customer
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth import hashers,authenticate,logout,login

# Create your views here.
# sign in view
def signin_view(request):
    return render(request, 'sign_in.html')



def register_view(request):
    if request.method =='POST':
        Customeremail = request.POST.get('Email')
        userpassword = request.POST.get('password')

        hashed_password = hashers.make_password(userpassword)
        new_user = Customer(
            Email=Customeremail,
            # username= useremail,
            password=hashed_password
        )
        new_user.save()
        return HttpResponse(request, 'registered successfully')
    else:
        return HttpResponse(request, 'not successfully')
    

def signin_auth(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user_auth_result = authenticate(request,username=email, password=password)
        if user_auth_result is not None:
            login(request, user_auth_result)
            return render(request, 'index.html')
        else:
            messages.error(request, "Invalid login details, check email or password")
            return render(request, 'sign_in.html')

def logout_view(request):
    logout(request)
    return redirect('index')

def index_view(request):
    return reverse('index')
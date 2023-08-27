from django.shortcuts import render

# Create your views here.
# sign up view

def signup_view(request):
    return render(request, 'sign_up.html')
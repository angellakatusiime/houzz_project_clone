from django.urls import path
from .views import signin_auth,signin_auth,signin_view,logout_view
urlpatterns = [
    path('',signin_view,name="index"),
    path('auth', signin_auth, name="sign_in_auth"),
    path('login', signin_auth, name="logout_view"),
    path('loggedout/', logout_view, name="logout"),
    
]
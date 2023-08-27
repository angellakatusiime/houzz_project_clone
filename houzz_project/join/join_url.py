from django.urls import path
from . import views
urlpatterns = [
    path('',views.join_view,name="join"),
    path('register_user/',views.register_view,name="register_user"),
]
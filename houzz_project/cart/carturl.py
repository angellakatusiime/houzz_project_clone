from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.cart_view, name='cart'),
    path('add_to_cart', views.add_to_cart_view, name='add_to_cart'),
    path('sell',views.sell_view, name='sell'),
]



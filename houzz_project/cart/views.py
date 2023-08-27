
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from .models import cart
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
# sale view
@login_required
def cart_view(request):
    return render(request, 'cart.html')



def add_to_cart_view(request):
    if request.method == 'POST':
        product_fetch = request.POST.get('pdt_name')
        quantity = request.POST.get('quantity')

        # Create a new cart object
        new_cart = cart(
            product=product_fetch,
            quantity=quantity,
            price=int(request.POST.get('price'))
        )
        new_cart.save()
        messages.success(request, "Item added successfully")

        return render(request, 'cart.html')
    

def sell_view(request):
    if request.method == 'GET':
        pdt_name = request.GET.get('pdt_name')

        context = {
            'pdt_name': pdt_name,
            'image': request.GET.get('image'),
            'price': request.GET.get('price'),

        }
        return render(request,'cart.html',context)

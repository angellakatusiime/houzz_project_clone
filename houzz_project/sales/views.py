from django.shortcuts import render

# Create your views here.
# sale view
def sale_view(request):
    return render(request, 'sale.html')
from django.shortcuts import render

def products_home(request):
    return render(request, 'order/products_home.html')
# Create your views here.

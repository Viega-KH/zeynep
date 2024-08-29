from django.shortcuts import render
from product.models import Products


def home(request):
    product_list = Products.objects.all().order_by('-created')[:3]
    return render(request, 'pages/home.html', {'product_list':product_list})

def about(request):
    product_list = Products.objects.all().order_by('-created')[:3]
    return render(request, 'pages/about.html', {'product_list':product_list})

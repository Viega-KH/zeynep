from django.shortcuts import render
from .models import Products
# Create your views here.
def product(request):
    product = Products.objects.all().order_by('-created')
    context = {
        'products':product
    }
    return render(request, 'pages/product.html', context)
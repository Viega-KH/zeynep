from django.shortcuts import render
from .models import Products
from django.core.paginator import Paginator


def product(request):
    search_query = request.GET.get('search', '')  # Get the search query from the URL
    
    if search_query:
        # Filter products by search query
        product_list = Products.objects.filter(title__icontains=search_query).order_by('-created')
    else:
        # Get all products if no search query is present
        product_list = Products.objects.all().order_by('-created')

    paginator = Paginator(product_list, 6)  # Number of products per page
    page_number = request.GET.get('page')  # Get current page number from URL
    page_obj = paginator.get_page(page_number)  # Get the page object

    context = {
        'page_obj': page_obj,
        'search_query': search_query  # Pass the search query to the template
    }
    return render(request, 'pages/product.html', context)

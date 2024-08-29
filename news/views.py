from django.shortcuts import render
from .models import News
from django.core.paginator import Paginator

def news(request):
    search_query = request.GET.get('search', '')
    if search_query:
        news_list = News.objects.filter(title__icontains=search_query).order_by('-created')
    else:
        news_list = News.objects.all().order_by('-created')
    
    paginator = Paginator(news_list, 10)  
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'search_query': search_query
    }
    return render(request, 'pages/news.html', context)


def newone(request, id):
    new = News.objects.get(id=id)
    context = {
        'new':new
    }
    return render(request, 'include/new.html', context)
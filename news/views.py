from django.shortcuts import render
from .models import News
# Create your views here.
def news(request):
    new = News.objects.all().order_by('-created')
    context = {
        'new':new
    }
    return render(request, 'pages/news.html', context)


def newone(request, id):
    new = News.objects.get(id=id)
    context = {
        'new':new
    }
    return render(request, 'include/new.html', context)
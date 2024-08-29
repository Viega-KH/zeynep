from django.urls import path
from .views import news, newone

urlpatterns = [
    path('news', news, name='news'),
    path('newone/<int:id>', newone, name='newone')
]

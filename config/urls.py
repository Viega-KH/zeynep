from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from django.views.static import serve
from django.urls import path, include, re_path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('', include('news.urls')),
    path('', include('product.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
]



urlpatterns += i18n_patterns(
    path('i18n/', include('django.conf.urls.i18n'), name='set_language'),
    path('', include('home.urls')),
    path('', include('news.urls')),
    path('', include('product.urls')),
    prefix_default_language=False  # Default til kodi URL'da ko'rsatilmasligi uchun
)

# Media fayllar uchun URL pattern
urlpatterns += [
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
]

# Statik fayllar uchun URL pattern
urlpatterns += [
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
]

# DEBUG rejimida media va statik fayllar uchun sozlamalar
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
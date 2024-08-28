from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from modeltranslation.translator import TranslationOptions, translator
from .models import News, Category


class NewsTranslationOptions(TranslationOptions):
    fields = ('title', 'body') 


translator.register(News, NewsTranslationOptions)

class CategoryTranslationOptions(TranslationOptions):
    fields = ('name',)  


translator.register(Category, CategoryTranslationOptions)


@admin.register(News)
class NewsAdmin(TranslationAdmin):
    list_display = ('title', 'categories', 'publish', )
    list_filter = ('publish', )
    search_fields = ('title', )
    fieldsets = (
        ('General Information', {
            'fields': ('categories', 'image', 'publish'),
            'classes': ('collapse',),
        }),
        ('Uzbek Content', {
            'fields': ('title_uz', 'body_uz'),
            'classes': ('collapse',),
        }),
        ('English Content', {
            'fields': ('title_en', 'body_en'),
            'classes': ('collapse',),
        }),
        ('Russian Content', {
            'fields': ('title_ru', 'body_ru'),
            'classes': ('collapse',),
        }),
        ('Turkish Content', {
            'fields': ('title_tr', 'body_tr'),
            'classes': ('collapse',),
        }),
    )


@admin.register(Category)
class CategoryAdmin(TranslationAdmin):
    pass
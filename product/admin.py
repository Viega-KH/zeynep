from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from modeltranslation.translator import TranslationOptions, translator
from .models import Products, Category


class ProductsTranslationOptions(TranslationOptions):
    fields = ('title',) 

translator.register(Products, ProductsTranslationOptions)

class CategoryTranslationOptions(TranslationOptions):
    fields = ('name',)  

translator.register(Category, CategoryTranslationOptions)


@admin.register(Products)
class ProductsAdmin(TranslationAdmin):
    list_display = ('title', 'categories', 'publish')
    list_filter = ('categories', 'publish')
    search_fields = ('title', 'categories__name')
    
    fieldsets = (
        ('General Information', {
            'fields': ('categories', 'image', 'publish'),
            'classes': ('collapse',),
        }),
        ('Uzbek Content', {
            'fields': ('title_uz',),
            'classes': ('collapse',),
        }),
        ('English Content', {
            'fields': ('title_en',),
            'classes': ('collapse',),
        }),
        ('Russian Content', {
            'fields': ('title_ru',),
            'classes': ('collapse',),
        }),
        ('Turkish Content', {
            'fields': ('title_tr',),
            'classes': ('collapse',),
        }),
    )


@admin.register(Category)
class CategoryAdmin(TranslationAdmin):
    pass

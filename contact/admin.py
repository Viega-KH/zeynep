from django.contrib import admin
from .models import Contact

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('location', 'telegram', 'instagram', 'call1', 'call2')

from django.contrib import admin
from .models import Contact

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'message', 'id')
    search_fields = ('name', 'email')
    list_filter = ('name', 'email')

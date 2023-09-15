from django.contrib import admin
from django.contrib.admin import ModelAdmin

from converter_api.models import Converter, ConverterSource


# Register your models here.
@admin.register(Converter)
class Converter(ModelAdmin):
    list_per_page = 5
    list_display = ['to_currency', 'from_currency', 'created', 'amount']
    list_filter = ['to_currency', 'from_currency', 'created']
    search_fields = ['to_currency', 'from_currency', 'created']
    date_hierarchy = 'created'
    ordering = ['-created']


@admin.register(ConverterSource)
class ConverterSource(ModelAdmin):
    list_per_page = 5
    list_display = ['currencies', 'created']
    list_filter = ['created']
    search_fields = ['created']
    date_hierarchy = 'created'
    ordering = ['-created']

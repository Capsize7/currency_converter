from django.contrib import admin
from django.contrib.admin import ModelAdmin

from converter_api.models import Converter, ConverterSource


# Register your models here.
@admin.register(Converter)
class Converter(ModelAdmin):
    """Configuration to represent Converter model on Admin site"""

    list_per_page = 5
    list_display = ['from_currency', 'to_currency', 'created', 'amount', 'result']
    list_filter = ['from_currency', 'to_currency', 'created']
    search_fields = ['from_currency', 'to_currency', 'created']
    date_hierarchy = 'created'
    ordering = ['-created']


@admin.register(ConverterSource)
class ConverterSource(ModelAdmin):
    """Configuration to represent ConverterSource model on Admin site"""

    list_per_page = 5
    list_display = ['currencies', 'created']
    list_filter = ['created']
    search_fields = ['created']
    date_hierarchy = 'created'
    ordering = ['-created']

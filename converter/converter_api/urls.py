from django.urls import path
from .views import ConverterList, ConverterSourceList, ConverterAPI

app_name = 'converter_api'

urlpatterns = [
    path('', ConverterList.as_view(), name='converters'),
    path('converter_source/', ConverterSourceList.as_view(), name='converter_source'),
    path('<str:to_currency>/<str:from_currency>/<int:amount>/', ConverterAPI.as_view(), name='converter'),
]

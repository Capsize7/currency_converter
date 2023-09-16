from django.urls import path
from .views import ConverterList, ConverterSourceList, ConverterAPI
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

app_name = 'converter_api'

urlpatterns = [
    path('', ConverterList.as_view(), name='converters'),
    path('converter_source/', ConverterSourceList.as_view(), name='converter_source'),
    path('<str:from_currency>/<str:to_currency>/<int:amount>/', ConverterAPI.as_view(), name='converter'),
    path("schema/", SpectacularAPIView.as_view(), name="schema_api"),
    path("schema/swagger-ui/", SpectacularSwaggerView.as_view(url_name="converter_api:schema_api"), name="swagger-ui")
]

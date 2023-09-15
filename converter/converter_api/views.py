from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from converter_api.models import Converter, ConverterSource
from converter_api.serializers import ConverterSerializer, ConverterSourceSerializer


# Create your views here.
class ConverterList(generics.ListAPIView):
    queryset = Converter.objects.all()
    serializer_class = ConverterSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['to_currency', 'from_currency', 'amount']
    search_fields = ['to_currency', 'from_currency']
    ordering_fields = ['created', 'to_currency', 'from_currency']


class ConverterSourceList(generics.ListAPIView):
    queryset = ConverterSource.objects.all()
    serializer_class = ConverterSourceSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    ordering_fields = ['created']


class ConverterAPI(APIView):
    def get(self, request, to_currency: str, from_currency: str, amount: int):
        converter_source = ConverterSource.objects.first().currencies
        print(converter_source)
        return Response({'posts': converter_source})

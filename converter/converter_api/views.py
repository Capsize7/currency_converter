from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from converter.tasks import pull_source
from converter_api.models import Converter, ConverterSource
from converter_api.serializers import ConverterSerializer, ConverterSourceSerializer


# Create your views here.
class ConverterList(generics.ListAPIView):
    """A view of all currencies conversion pairs which have been requested. Allowed methods: GET"""

    queryset = Converter.objects.all()
    serializer_class = ConverterSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['to_currency', 'from_currency', 'amount']
    search_fields = ['to_currency', 'from_currency']
    ordering_fields = ['created', 'to_currency', 'from_currency']


class ConverterSourceList(generics.ListAPIView):
    """A view of all source data for currencies conversion. Allowed methods: GET"""

    queryset = ConverterSource.objects.all()
    serializer_class = ConverterSourceSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    ordering_fields = ['created']


class ConverterAPI(APIView):
    """
    A main view of conversion currencies pairs.
    Allowed methods: GET
    """

    def get(self, request, from_currency: str, to_currency: str, amount: int):
        """
        The main method to get source data if it doesn't exist yet or get it from database.
        Checking send data with serializer and additional tools.
        Preparing an answer of currencies pair conversion and write it in database.
        """

        from_currency = from_currency.upper()
        to_currency = to_currency.upper()
        if ConverterSource.objects.count() == 0:
            pull_source()
        converter_source = ConverterSource.objects.first().currencies
        if not converter_source['Valute'].get(to_currency) or not converter_source['Valute'].get(from_currency):
            return Response({'result': 'There is not currency pair'})
        ser = ConverterSerializer(data=
                                  {'from_currency': from_currency, 'to_currency': to_currency,
                                   'amount': amount})
        if not ser.is_valid():
            return Response({'result': 'Not valid data for currency pair'})

        result = converter_source['Valute'].get(from_currency)['Value'] / converter_source['Valute'].get(to_currency)[
            'Value'] * amount
        result_data = ser.data
        result_data.update({'result': result})
        Converter.objects.create(to_currency=to_currency, from_currency=from_currency, result=result, amount=amount)
        return Response(result_data)

from rest_framework.serializers import ModelSerializer

from converter_api.models import Converter, ConverterSource


class ConverterSerializer(ModelSerializer):
    class Meta:
        model = Converter
        fields = ['to_currency', 'from_currency', 'created', 'amount']


class ConverterSourceSerializer(ModelSerializer):
    class Meta:
        model = ConverterSource
        fields = ['currencies', 'created']

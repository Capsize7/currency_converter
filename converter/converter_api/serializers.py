from rest_framework.serializers import ModelSerializer

from converter_api.models import Converter, ConverterSource


class ConverterSerializer(ModelSerializer):
    '''Simple model based serializer for pairs of currencies conversion'''
    
    class Meta:
        model = Converter
        fields = ['to_currency', 'from_currency', 'created', 'amount']


class ConverterSourceSerializer(ModelSerializer):
    '''Simple model based serializer for source data of currencies conversion'''
    
    class Meta:
        model = ConverterSource
        fields = ['currencies', 'created']

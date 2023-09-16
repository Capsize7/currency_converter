import datetime
import json
import requests
from django.test import TestCase
from django.urls import reverse

from converter_api.models import Converter, ConverterSource
from converter_api.serializers import ConverterSerializer, ConverterSourceSerializer


class ConverterSerializerTestCase(TestCase):
    """Testing serializers to check serialized data"""

    def test_create(self):
        expected_data = {'from_currency': 'USD', 'to_currency': 'RUB',
                         'amount': 1}
        data = ConverterSerializer(expected_data).data
        self.assertEqual(data, expected_data)


class ConverterSourceSerializerTestCase(TestCase):
    """Testing serializers to check serialized data"""

    def test_create(self):
        source_json = json.loads(requests.get('https://www.cbr-xml-daily.ru/daily_json.js').content)
        time_now = datetime.datetime.now()
        expected_data = {'currencies': source_json, 'created': time_now.isoformat()}
        data = ConverterSourceSerializer(expected_data).data
        self.assertEqual(data, expected_data)


class ConverterURLsTest(TestCase):
    """Testing URLs to check returning status code and requested view"""

    def test_converter_url_name(self):
        response = self.client.get(reverse('converter_api:converter_source'))
        self.assertEqual(response.status_code, 200)

    def test_converters_url_name(self):
        response = self.client.get(reverse('converter_api:converters'))
        self.assertEqual(response.status_code, 200)

    def test_converter_source_url_name(self):
        response = self.client.get(reverse('converter_api:converter', args=['USD', 'RUB', 1]))
        self.assertEqual(response.status_code, 200)


class ConverterConverterSourceModelTest(TestCase):
    """Testing Converter and ConverterSource model to check creation and retrieving data from these models"""

    def setUp(self) -> None:
        self.source_json = json.loads(requests.get('https://www.cbr-xml-daily.ru/daily_json.js').content)
        self.converter = Converter.objects.create(to_currency='USD', from_currency='USD', amount=1)
        self.converter_source = ConverterSource.objects.create(currencies=self.source_json)

    def test_create_converter(self):
        self.assertIsInstance(self.converter, Converter)

    def test_create_converter_source(self):
        self.assertIsInstance(self.converter_source, ConverterSource)

    def test_saving_and_retrieving_converter(self):
        self.converter.save()
        saved_converter = Converter.objects.all()
        self.assertEquals(saved_converter.count(), 1)
        self.assertEquals(self.converter.from_currency, 'USD')

    def test_saving_and_retrieving_converter_source(self):
        self.converter_source.save()
        saved_converter_source = ConverterSource.objects.all()
        self.assertEquals(saved_converter_source.count(), 1)
        self.assertEquals(self.converter_source.currencies, self.source_json)

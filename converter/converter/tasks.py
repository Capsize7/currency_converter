import json
import requests
from celery import shared_task


@shared_task
def pull_source():
    """A simple celery task to get source data and update it every hour
     for conversion currencies pairs via request of open API rates
    """

    from converter_api.models import ConverterSource
    source_json = json.loads(requests.get('https://www.cbr-xml-daily.ru/daily_json.js').content)
    source_json['Valute']['RUB'] = {'Name': 'Российский рубль', 'Value': 1}
    ConverterSource.objects.create(currencies=source_json)

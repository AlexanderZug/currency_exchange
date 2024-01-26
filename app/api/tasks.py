import requests

from celery import shared_task

from .models import CurrencyRate


CBRF_URL="https://www.cbr-xml-daily.ru/daily_json.js"


@shared_task
def get_currency_rate():
    data = requests.get(CBRF_URL).json()
    exchange_rate = data['Valute']['USD']

    CurrencyRate.objects.create(rate=exchange_rate)

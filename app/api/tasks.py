import os
import requests

from celery import shared_task

from .models import CurrencyRate


@shared_task
def get_currency_rate():
    data = requests.get(os.environ.get('CBRF_URL')).json()
    exchange_rate = data['Valute']['USD']

    CurrencyRate.objects.create(rate=exchange_rate)

import os
import requests

from django.shortcuts import render


def currency_view(request):
    data = requests.get(os.environ.get('CBRF_URL')).json()
    exchange_rate = data['Valute']['USD']

    return render(request, 'currency.html', {'exchange_rate': exchange_rate})

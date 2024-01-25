from django.shortcuts import render

from .models import CurrencyRate


def currency_view(request):
    latest_rates = CurrencyRate.objects.order_by('-id')[:10]

    exchange_rate = [rate.rate for rate in latest_rates]

    return render(request, 'currency.html', {'exchange_rate': exchange_rate})

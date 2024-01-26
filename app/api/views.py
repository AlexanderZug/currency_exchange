from django.shortcuts import render

from .models import CurrencyRate


def delete_all_records_except_last_ten():
    latest_ids = CurrencyRate.objects.order_by('-id')[:10].values_list('id', flat=True)
    CurrencyRate.objects.exclude(id__in=latest_ids).delete()


def currency_view(request):
    delete_all_records_except_last_ten()

    latest_rates = CurrencyRate.objects.order_by('-id')
    exchange_rate = [rate.rate for rate in latest_rates]

    return render(request, 'currency.html', {'exchange_rate': exchange_rate})

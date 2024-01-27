from django.test import TestCase
from django.shortcuts import reverse
from .models import CurrencyRate
from .views import delete_all_records_except_last_ten


class CurrencyViewTests(TestCase):

    def setUp(self):
        for i in range(15):
            CurrencyRate.objects.create(rate={'value': i})

    def test_delete_all_records_except_last_ten(self):
        delete_all_records_except_last_ten()
        self.assertEqual(CurrencyRate.objects.count(), 10)

    def test_currency_view(self):
        response = self.client.get(reverse('currency_view'))
        self.assertEqual(response.status_code, 200)

        self.assertTrue('exchange_rate' in response.context)

        exchange_rate = response.context['exchange_rate']
        self.assertEqual(len(exchange_rate), 10)

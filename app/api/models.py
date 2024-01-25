from django.db import models


class CurrencyRate(models.Model):
    rate = models.JSONField("Курс валюты")

    def __str__(self):
        return str(self.rate)

    class Meta:
        verbose_name = "Курс валюты"
        verbose_name_plural = "Курсы валют"

import os

from celery import Celery


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'exchange_currency.settings')

app = Celery('exchange_currency')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

app.conf.beat_schedule = {
    'get_rate': {
        'task': 'api.tasks.get_currency_rate',
        'schedule': 10.0,
    }
}

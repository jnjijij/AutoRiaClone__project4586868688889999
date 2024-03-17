import requests

from backend.configs import models


def get_exchange_rate(base_currency, target_currency):
    global target_rate, base_rate
    url = f'https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5'
    response = requests.get(url)
    data = response.json()
    for item in data:
        if item['ccy'] == base_currency:
            base_rate = item['sale']
        if item['ccy'] == target_currency:
            target_rate = item['sale']
    return target_rate / base_rate

def update_exchange_rates(CURRENCIES=None):
    for currency in CURRENCIES:
        rate = get_exchange_rate('UAH', currency)
        CurrencyRate.objects.update_or_create(
            currency=currency,
            defaults={'rate': rate},
        )

class CurrencyRate(models.Model):
    objects = None
    currency = models.CharField(max_length=3)
    rate = models.DecimalField(max_digits=10, decimal_places=2)
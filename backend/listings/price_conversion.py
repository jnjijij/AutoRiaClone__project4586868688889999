import requests

def get_exchange_rates():
    response = requests.get('https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5')
    data = response.json()
    return {rate['ccy']: rate['buy'] for rate in data}

def convert_price(price, currency, target_currency):
    exchange_rates = get_exchange_rates()
    buy_rate = exchange_rates[currency]
    target_buy_rate = exchange_rates[target_currency]
    return price * (target_buy_rate / buy_rate)
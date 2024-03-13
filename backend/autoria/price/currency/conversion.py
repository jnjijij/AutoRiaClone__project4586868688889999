import requests

def convert_currency(amount, from_currency, to_currency):
    # Make an API request to get the exchange rate
    response = requests.get(f'https://api.privatbank.ua/p24api/pubinfo?exchange&json&coursid=11')
    data = response.json()

    # Extract the exchange rate for the specified currencies
    exchange_rates = {entry['ccy']: float(entry['buy']) for entry in data}
    if from_currency in exchange_rates and to_currency in exchange_rates:
        rate = exchange_rates[to_currency] / exchange_rates[from_currency]
        converted_amount = amount * rate
        return converted_amount, rate
    else:
        return None, None

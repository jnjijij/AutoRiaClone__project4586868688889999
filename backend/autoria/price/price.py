import requests
from flask import Flask, jsonify, request

app = Flask(__name__)

cars = [
    {'brand': 'bmw', 'model': 'x5', 'category': 'economy', 'price': {'usd': 1000, 'eur': 800, 'uah': 20000}, 'currency': 'usd', 'user_id': 1},
    {'brand': 'daewoo', 'model': 'lanos', 'category': 'mid-range', 'price': {'usd': 500, 'eur': 400, 'uah': 10000}, 'currency': 'usd', 'user_id': 2},
    {'brand': 'bmw', 'model': 'x5', 'category': 'high-end', 'price': {'usd': 2000, 'eur': 1600, 'uah': 30000}, 'currency': 'usd', 'user_id': 3},
    {'brand': 'daewoo', 'model': 'lanos', 'category': 'economy', 'price': {'usd': 1000, 'eur': 800, 'uah': 20000}, 'currency': 'usd', 'user_id': 4},
]

def check_profanity(text):
    url = "https://www.purgomalum.com/service/plain?text=" + text
    response = requests.get(url)
    return response.text != text

@app.route('/api/cars', methods=['POST'])
def create_car():
    brand = request.json['brand']
    model = request.json['model']
    category = request.json['category']
    price = request.json['price']
    currency = request.json['currency']
    user_id = request.json['user_id']

    if check_profanity(brand) or check_profanity(model) or check_profanity(category):
        return jsonify({'error': 'Profanity detected'}), 400

    if price['usd'] is None or price['eur'] is None or price['uah'] is None:
        return jsonify({'error': 'Price in all currencies is required'}), 400

    if currency not in ['usd', 'eur', 'uah']:
        return jsonify({'error': 'Invalid currency'}), 400

    car = {
        'brand': brand,
        'model': model,
        'category': category,
        'price': price,
        'currency': currency,
        'user_id': user_id,
    }

    cars.append(car)

    return jsonify(car), 201

@app.route('/api/cars', methods=['GET'])
def get_cars():
    brand = request.args.get('brand')
    model = request.args.get('model')
    category = request.args.get('category')

    filtered_cars = [car for car in cars if car['brand'] == brand and car['model'] == model and car['category'] == category]

    return jsonify(filtered_cars)

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

cars = [
    {'brand': 'toyota', 'model': 'camry', 'category': 'mid-range', 'price': {'usd': 1000, 'eur': 800, 'uah': 20000}, 'currency': 'usd', 'user_id': 1, 'edit_count': 0},
    {'brand': 'daewoo', 'model': 'lanos', 'category': 'mid-range', 'price': {'usd': 500, 'eur': 400, 'uah': 10000}, 'currency': 'usd', 'user_id': 2, 'edit_count': 0},
    {'brand': 'bmw', 'model': 'x5', 'category': 'high-end', 'price': {'usd': 2000, 'eur': 1600, 'uah': 30000}, 'currency': 'usd', 'user_id': 3, 'edit_count': 0},
    {'brand': 'daewoo', 'model': 'lanos', 'category': 'economy', 'price': {'usd': 1000, 'eur': 800, 'uah': 20000}, 'currency': 'usd', 'user_id': 4, 'edit_count': 0},
]

def check_profanity(text):
    url = "https://www.purgomalum.com/service/plain?text=" + text
    response = requests.get(url)
    return response.text != text

def edit_car(car_id, new_data):
    car = get_car_by_id(car_id)

    if car['edit_count'] >= 3:
        return jsonify({'error': 'Car is not active'}), 400

    if check_profanity(new_data['brand']) or check_profanity(new_data['model']) or check_profanity(new_data['category']):
        return jsonify({'error': 'Profanity detected'}), 400

    if new_data['price']['usd'] is None or new_data['price']['eur'] is None or new_data['price']['uah'] is None:
        return jsonify({'error': 'Price in all currencies is required'}), 400

    if new_data['currency'] not in ['usd', 'eur', 'uah']:
        return jsonify({'error': 'Invalid currency'}), 400

    car['brand'] = new_data['brand']
    car['model'] = new_data['model']
    car['category'] = new_data['category']
    car['price'] = new_data['price']
    car['currency'] = new_data['currency']
    car['edit_count'] += 1

    return jsonify(car), 200

def get_car_by_id(car_id):
    for car in cars:
        if car['user_id'] == car_id:
            return car

    return None

@app.route('/api/cars', methods=['POST'])
def create_car():


@app.route('/api/cars', methods=['GET'])
def get_cars():


@app.route('/api/cars/<int:car_id>', methods=['PUT'])
def update_car(car_id):
    new_data = request.json

    return edit_car(car_id, new_data)

if __name__ == '__main__':
    app.run(debug=True)
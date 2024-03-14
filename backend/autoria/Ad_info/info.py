from flask import Flask, request, jsonify
from profanityfilter import ProfanityFilter
from sqlalchemy.testing import db

from backend.my_project.models import Car

app = Flask(__name__)

cars = [

]


def check_profanity(text):
    profanity_filter = ProfanityFilter()
    return profanity_filter.is_profane(text)


def edit_car(car_id, new_data):
    car = Car.query.get(car_id)

    if not car:
        return jsonify({'error': 'Car not found'}), 404

    for key, value in new_data.items():
        if hasattr(car, key):
            setattr(car, key, value)

    db.session.commit()

    return jsonify({'message': 'Car updated successfully'}), 200


def get_car_by_id(car_id):
    car = Car.query.get(car_id)

    if not car:
        return jsonify({'error': 'Car not found'}), 404

    return jsonify({'car': car.to_dict()}), 200


def get_car_ads_info(car_id):
    car = get_car_by_id(car_id)

    if car is None:
        return jsonify({'error': 'Car not found'}), 404

    views_count = 0
    views_by_period = {'day': 0, 'week': 0, 'month': 0}
    avg_price_by_region = {'kyiv': 0, 'lviv': 0, 'all': 0}

    for car in cars:
        if car['user_id'] == car_id:
            views_count += 1

            if car['category'] == 'economy':
                avg_price_by_region['kyiv'] += car['price']['uah']
                avg_price_by_region['lviv'] += car['price']['uah']
                avg_price_by_region['all'] += car['price']['uah']

    for car in cars:
        if car['user_id'] == car_id:
            if car['category'] == 'economy':
                views_by_period['day'] += 1
                views_by_period['week'] += 1
                views_by_period['month'] += 1

    avg_price_by_region['kyiv'] /= views_count
    avg_price_by_region['lviv'] /= views_count
    avg_price_by_region['all'] /= views_count

    return jsonify({
        'views_count': views_count,
        'views_by_period': views_by_period,
        'avg_price_by_region': avg_price_by_region
    })


@app.route('/api/cars', methods=['POST'])
def create_car():
    data = request.json
    if 'brand' not in data or 'model' not in data or 'year' not in data:
        return jsonify({'error': 'Missing required fields'}), 400
    new_car = {
        'brand': data['brand'],
        'model': data['model'],
        'year': data['year'],
        'color': data.get('color', 'N/A')
    }
    cars.append(new_car)

    return jsonify({'message': 'Car created successfully', 'car': new_car}), 201


@app.route('/api/cars', methods=['GET'])
def get_cars():
    return jsonify({'cars': cars})


@app.route('/api/cars/<int:car_id>', methods=['PUT'])
def update_car(car_id):
    new_data = request.json

    return edit_car(car_id, new_data)


@app.route('/api/cars/<int:car_id>/ads_info', methods=['GET'])
def get_car_ads_info_endpoint(car_id):
    return get_car_ads_info(car_id)


if __name__ == '__main__':
    app.run(debug=True)

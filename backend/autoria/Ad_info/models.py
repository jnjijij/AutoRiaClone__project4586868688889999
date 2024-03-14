from urllib import request

from flask import jsonify

from backend.autoria.Ad_info.info import check_profanity, edit_car
from frontend.system.cars_search import app


@app.route('/api/cars', methods=['POST'])
def create_car():
    new_data = request.json

    if check_profanity(new_data['title']):
        return jsonify({'error': 'Profanity is not allowed'}), 400

@app.route('/api/cars/<int:car_id>', methods=['PUT'])
def update_car(car_id):
    new_data = request.json

    return edit_car(car_id, new_data)
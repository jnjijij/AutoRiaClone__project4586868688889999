from flask import Flask, jsonify, request

app = Flask(__name__)

cars = [
    {'brand': 'bmw', 'model': 'x5', 'category': 'economy'},
    {'brand': 'daewoo', 'model': 'lanos', 'category': 'mid-range'},
    {'brand': 'bmw', 'model': 'x5', 'category': 'high-end'},
    {'brand': 'daewoo', 'model': 'lanos', 'category': 'economy'},
]

@app.route('/api/cars', methods=['GET'])
def get_cars():
    brand = request.args.get('brand')
    model = request.args.get('model')
    category = request.args.get('category')

    filtered_cars = [car for car in cars if car['brand'] == brand and car['model'] == model and car['category'] == category]

    return jsonify(filtered_cars)

if __name__ == '__main__':
    app.run(debug=True)
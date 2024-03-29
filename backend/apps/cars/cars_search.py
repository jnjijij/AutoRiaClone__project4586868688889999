from django.http import JsonResponse
from django.shortcuts import render

cars = [
    {'brand': 'bmw', 'model': 'x5', 'category': 'economy'},
    {'brand': 'daewoo', 'model': 'lanos', 'category': 'mid-range'},
    {'brand': 'bmw', 'model': 'x5', 'category': 'high-end'},
    {'brand': 'daewoo', 'model': 'lanos', 'category': 'economy'},
]

def get_cars(request):
    brand = request.GET.get('brand')
    model = request.GET.get('model')
    category = request.GET.get('category')

    filtered_cars = [car for car in cars if car['brand'] == brand and car['model'] == model and car['category'] == category]

    return JsonResponse(filtered_cars, safe=False)
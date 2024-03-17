import requests
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt

from django.http import HttpResponse

cars = [
    {'brand': 'bmw', 'model': 'x5', 'category': 'economy', 'price': {'usd': 1000, 'eur': 800, 'uah': 20000},
     'currency': 'usd', 'user_id': 1},
    {'brand': 'daewoo', 'model': 'lanos', 'category': 'mid-range', 'price': {'usd': 500, 'eur': 400, 'uah': 10000},
     'currency': 'usd', 'user_id': 2},
    {'brand': 'bmw', 'model': 'x5', 'category': 'high-end', 'price': {'usd': 2000, 'eur': 1600, 'uah': 30000},
     'currency': 'usd', 'user_id': 3},
    {'brand': 'daewoo', 'model': 'lanos', 'category': 'economy', 'price': {'usd': 1000, 'eur': 800, 'uah': 20000},
     'currency': 'usd', 'user_id': 4},
]


def check_profanity(text):
    url = "https://www.purgomalum.com/service/plain?text=" + text
    response = requests.get(url)
    return response.text != text


@csrf_exempt
@require_http_methods(['POST'])
def create_car(request):
    brand = request.POST.get('brand')
    model = request.POST.get('model')
    category = request.POST.get('category')
    price = request.POST.get('price')
    currency = request.POST.get('currency')
    user_id = request.POST.get('user_id')

    if check_profanity(brand) or check_profanity(model) or check_profanity(category):
        return JsonResponse({'error': 'Profanity detected'}, status=400)

    if not all([price['usd'], price['eur'], price['uah']]):
        return JsonResponse({'error': 'Price in all currencies is required'}, status=400)

    if currency not in ['usd', 'eur', 'uah']:
        return JsonResponse({'error': 'Invalid currency'}, status=400)

    car = {
        'brand': brand,
        'model': model,
        'category': category,
        'price': price,
        'currency': currency,
        'user_id': user_id,
    }

    cars.append(car)

    return JsonResponse(car, status=201)


@csrf_exempt
@require_http_methods(['GET'])
def get_cars(request):
    brand = request.GET.get('brand')
    model = request.GET.get('model')
    category = request.GET.get('category')

    filtered_cars = [car for car in cars if
                     car['brand'] == brand and car['model'] == model and car['category'] == category]

    return JsonResponse(filtered_cars, safe=False)


def index(request):
    return HttpResponse("Hello, World!")

from django.forms import model_to_dict
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_GET, require_http_methods

from .models import Car
from .price import check_profanity


@csrf_exempt
@require_http_methods(["POST"])
def create_car(request):
    new_data = request.POST
    return edit_car(None, new_data)


@require_GET
def get_cars():
    # Assuming you have a Car model in your Django app
    cars = Car.objects.all().values()
    return JsonResponse(list(cars), safe=False)


@csrf_exempt
@require_http_methods(["PUT"])
def update_car(request, car_id):
    new_data = request.POST
    return edit_car(car_id, new_data)


def edit_car(car_id, new_data):
    car = get_car_by_id(car_id)

    if car and car['edit_count'] >= 3:
        return JsonResponse({'error': 'Car is not active'}, status=400)

    if check_profanity(new_data['brand']) or check_profanity(new_data['model']) or check_profanity(new_data['category']):
        return JsonResponse({'error': 'Profanity detected'}, status=400)

    if new_data['price_usd'] is None or new_data['price_eur'] is None or new_data['price_uah'] is None:
        return JsonResponse({'error': 'Price in all currencies is required'}, status=400)

    if new_data['currency'] not in ['usd', 'eur', 'uah']:
        return JsonResponse({'error': 'Invalid currency'}, status=400)

    car.brand = new_data['brand']
    car.model = new_data['model']
    car.category = new_data['category']
    car.price_usd = new_data['price_usd']
    car.price_eur = new_data['price_eur']
    car.price_uah = new_data['price_uah']
    car.currency = new_data['currency']
    car.edit_count += 1
    car.save()

    return JsonResponse(model_to_dict(car))


def get_car_by_id(car_id):
    try:
        return Car.objects.get(user_id=car_id)
    except Car.DoesNotExist:
        return None
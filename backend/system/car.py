from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from .models import Car, CarAd, CarAdView
from .forms import CarForm

def index(request):
    cars = Car.objects.all()
    return render(request, 'index.html', {'cars': cars})

def get_car_by_id(request, car_id):
    car = get_object_or_404(Car, pk=car_id)
    return JsonResponse(car.to_dict())

def edit_car(request, car_id):
    car = get_object_or_404(Car, pk=car_id)
    if request.method == 'POST':
        form = CarForm(request.POST, instance=car)
        if form.is_valid():
            form.save()
            return redirect('get_car_by_id', car_id=car_id)
    else:
        form = CarForm(instance=car)
    return render(request, 'edit_car.html', {'form': form})

def get_car_ads_info(request, car_id):
    car = get_object_or_404(Car, pk=car_id)
    views_count = CarAdView.objects.filter(car_id=car_id).count()
    views_by_period = CarAdView.objects.filter(car_id=car_id).order_by('-timestamp')[:10]
    avg_price_by_region = CarAd.objects.filter(car_id=car_id).values('region').annotate(avg_price=('price'))
    response_data = {
        'car': car.to_dict(),
        'views_count': views_count,
        'views_by_period': [view.to_dict() for view in views_by_period],
        'avg_price_by_region': [{'region': item['region'], 'avg_price': item['avg_price']} for item in avg_price_by_region]
    }
    return JsonResponse(response_data)

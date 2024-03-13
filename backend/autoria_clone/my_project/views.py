from rest_framework import viewsets
from models import Car, CarPrice
from serializers import CarSerializer, CarPriceSerializer

class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

class CarPriceViewSet(viewsets.ModelViewSet):
    queryset = CarPrice.objects.all()
    serializer_class = CarPriceSerializer

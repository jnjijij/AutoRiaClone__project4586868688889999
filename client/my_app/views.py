from rest_framework import viewsets
from rest_framework import viewsets
from .models import CarBrand, CarModel, CarPrice
from .serializers import CarBrandSerializer, CarModelSerializer, CarPriceSerializer
from django.shortcuts import render
from .models import Client

class CarBrandViewSet(viewsets.ModelViewSet):
    queryset = CarBrand.objects.all()
    serializer_class = CarBrandSerializer

class CarModelViewSet(viewsets.ModelViewSet):
    queryset = CarModel.objects.all()
    serializer_class = CarModelSerializer

class CarPriceViewSet(viewsets.ModelViewSet):
    queryset = CarPrice.objects.all()
    serializer_class = CarPriceSerializer

def client_list(request):
    clients = Client.objects.all()
    return render(request, 'clients/client_list.html', {'clients': clients})

def client_detail(request, pk):
    client = Client.objects.get(id=pk)
    return render(request, 'clients/client_detail.html', {'client': clien

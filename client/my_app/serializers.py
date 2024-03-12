from rest_framework import serializers
from .models import CarBrand, CarModel, CarPrice

class CarBrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarBrand
        fields = '__all__'

class CarModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarModel
        fields = '__all__'

class CarPriceSerializer(serializers.ModelSerializer):
    car_model = CarModelSerializer(read_only=True)

    class Meta:
        model = CarPrice
        fields = '__all__'

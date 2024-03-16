from rest_framework import serializers
from .models import Park


class ParkSerializer:
    def __init__(self):
        self.data = None

    pass

    def is_valid(self):
        pass

    def save(self):
        pass


class ParkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Park
        fields = ('id', 'name', 'address', 'city', 'state', 'zip_code', 'country', 'description')
        park = Park.objects.get(id=1)
        serializer = ParkSerializer()
        serialized_data = serializer.data
        data = {
            'name': 'Test Park',
            'address': '123 Test St',
            'city': 'Test City',
            'state': 'Test State',
            'zip_code': '12345',
            'country': 'Test Country',
            'description': 'This is a test park.'
        }
        serializer = ParkSerializer(data=data)
        serializer.is_valid()
        park = serializer.save()


class CarParkSerializer:
    def __init__(self):
        self.data = None

    pass
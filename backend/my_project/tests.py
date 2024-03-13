from django.test import TestCase

from models import Car


class CarTestCase(TestCase):
    def setUp(self):
        Car.objects.create(brand='BMW', model='X5', price=100)

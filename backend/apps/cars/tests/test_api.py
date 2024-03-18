from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from apps.cars.models import CarModel

UserModel = get_user_model()


class CarApiTestCase(APITestCase):
    def _authenticate(self):
        email = 'admin@gmail.com'
        password = 'P@$$word1'
        self.client.post(reverse('user_create'), {
            "email": email,
            "password": password,
            "profile": {
                "name": "Max",
                "surname": "Popov",
                "age": 30
            }
        }, format='json')
        user = UserModel.objects.get(email=email)
        user.is_active = True
        user.save()
        response = self.client.post(reverse('auth_login'), {'email': email, 'password': password})
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {response.data["access"]}')

    def test_cars_create_without_auth(self):
        sample_car = {
            'brand': 'BMW',
            'price': 2000,
            'year': 2005,
            'body_type': 'Jeep'
        }
        response = self.client.post(reverse('cars_list_create'), sample_car)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(CarModel.objects.count(), 0)

    def test_cars_create_with_auth(self):
        self._authenticate()
        sample_car = {
            'brand': 'BMW',
            'price': 2000,
            'year': 2005,
            'body_type': 'Jeep'
        }
        response = self.client.post(reverse('cars_list_create'), sample_car)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(CarModel.objects.count(), 1)

from django.test import TestCase
from django.urls import reverse

from backend.autoria.autoria.models import Image
from backend.my_project.models import Car


class ImageTestCase(TestCase):
    def setUp(self):
        self.car = Car.objects.create(brand='Toyota', model='Camry', year=2020)
        self.image = Image.objects.create(car=self.car, image='images/test_image.jpg')

    def test_add_image(self):
        response = self.client.post(reverse('add_image', args=[self.car.id]), {'image': 'images/test_image2.jpg'})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Image.objects.count(), 2)
        self.assertEqual(Image.objects.latest('id').image.name, 'images/test_image2.jpg')

    def test_update_image(self):
        response = self.client.post(reverse('update_image', args=[self.car.id]), {'image': 'images/test_image3.jpg'})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Image.objects.count(), 1)
        self.assertEqual(Image.objects.get(id=self.image.id).image.name, 'images/test_image3.jpg')

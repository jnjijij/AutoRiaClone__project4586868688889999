from django.db import models
from django.urls import reverse

class Park(models.Model):
    objects = None
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=10)
    country = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('park-detail', args=[str(self.id)])


class CarPark:
    DoesNotExist = None
    objects = None
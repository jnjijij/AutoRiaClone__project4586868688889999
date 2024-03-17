
from django.db import models

from backend.database import Car
from backend.listings.models import Account


class Advertisement(models.Model):
    objects = None
    price = models.DecimalField(max_digits=10, decimal_places=2)

class Advertisement(models.Model):
    STATUSES = (
        ('active', 'Активне'),
        ('inactive', 'Неактивне'),
    )
    seller = models.ForeignKey(Account, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=3)
    status = models.CharField(max_length=10, choices=STATUSES)
    views = models.IntegerField(default=0)

class AdvertisementStatistics(models.Model):
    objects = None
    advertisement = models.OneToOneField(Advertisement, on_delete=models.CASCADE)
    views = models.IntegerField(default=0)
    daily_views = models.IntegerField(default=0)
    weekly_views =models.IntegerField(default=0)
    monthly_views = models.IntegerField(default=0)
    regional_price = models.DecimalField(max_digits=10, decimal_places=2)
    national_price = models.DecimalField(max_digits=10, decimal_places=2)
class CarBrand(models.Model):
    name = models.CharField(max_length=100)

class CarModel(models.Model):
    brand = models.ForeignKey(CarBrand, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

class Advertisement(models.Model):
    ...
    brand = models.ForeignKey(CarBrand, on_delete=models.CASCADE)
    model = models.ForeignKey(CarModel, on_delete=models.CASCADE)
    ...
    
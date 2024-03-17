
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
    brand = models.ForeignKey(CarBrand, on_delete=models.CASCADE)
    model = models.ForeignKey(CarModel, on_delete=models.CASCADE)

class Advertisement(models.Model):
    MARKA_CHOICES = (
        ('toyota', 'Toyota'),
        ('ford', 'Ford'),
        ('bmw', 'BMW'),
        # ...
    )

    STATUS_CHOICES = (
        ('active', 'Активне'),
        ('inactive', 'Не активне'),
        ('verification', 'Перевірка'),
    )

    marka = models.CharField(max_length=20, choices=MARKA_CHOICES)
    model = models.CharField(max_length=20)
    currency = models.CharField(max_length=10)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    date_of_advertisement = models.DateTimeField(auto_now_add=True)
    date_of_editing = models.DateTimeField(auto_now=True)
    views = models.IntegerField(default=0)

class Advertisement(models.Model):
    # ...
    edit_attempts = models.IntegerField(default=0)

def save(self, *args, **kwargs):
    if self.status == 'verification' and self.edit_attempts >= 3:
        self.status = 'verification'
        self.edit_attempts = 0
    elif self.status == 'verification' and self.edit_attempts < 3:
        self.edit_attempts += 1
    super().save(*args, **kwargs)

    
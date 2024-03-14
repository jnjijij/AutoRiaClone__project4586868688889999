from django.db import models

class Car(models.Model):
    query = None
    objects = None
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=3, choices=[('USD', 'USD'), ('EUR', 'EUR'), ('UAH', 'UAH')])
    region = models.CharField(max_length=100)

class CarPrice(models.Model):
    objects = None
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=3, choices=[('USD', 'USD'), ('EUR', 'EUR'), ('UAH', 'UAH')])
    date = models.DateField()

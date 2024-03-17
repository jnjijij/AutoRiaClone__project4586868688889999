from django.db import models
from django.contrib.auth.models import User

from backend.listings.models import Role


class MotorshowDealer(models.Model):
    address = models.CharField(max_length=200)
    name = models.CharField(max_length=155)
    phone = models.CharField(max_length=20)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
class Autosalon(models.Model):
    objects = None
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    manager = models.ForeignKey('clients.Client', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Client:
    objects = None


class DealerForm:
    def is_valid(self):
        pass

    def save(self):
        pass


class Dealer:
    pass
class Advertisement(models.Model):
    objects = None
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=3)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Autosaloon:
    pass

class CarDealer(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    manager = models.ForeignKey(Role, on_delete=models.CASCADE, related_name='car_dealer_manager')
    admin = models.ForeignKey(Role, on_delete=models.CASCADE, related_name='car_dealer_admin')
    sales = models.ManyToManyField(Role, related_name='car_dealer_sales')
    mechanics = models.ManyToManyField(Role, related_name='car_dealer_mechanics')
from django.db import models
from django.contrib.auth.models import User

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

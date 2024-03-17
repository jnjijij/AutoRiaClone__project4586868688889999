from django.db import models


class Car(models.Model):
    objects = None
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name


class CarBrand:
    pass


class CarModel:
    pass


class CarPrice:
    pass


class User:
    pass


def Ad():
    return None


class CarListing:
    objects = None

class Car(models.Model):
    brand = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    year = models.IntegerField()
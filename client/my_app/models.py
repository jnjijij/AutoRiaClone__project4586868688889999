from django.db import models

class CarBrand(models.Model):
    objects = None
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class CarModel(models.Model):
    objects = None
    brand = models.ForeignKey(CarBrand, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class CarPrice(models.Model):
    objects = None
    car_model = models.ForeignKey(CarModel, on_delete=models.CASCADE)
    currency = models.CharField(max_length=3)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.car_model.name} - {self.price} {self.currency}"


class Client:
    objects = None

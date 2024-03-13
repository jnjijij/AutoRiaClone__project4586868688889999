from django.db import models

class Image(models.Model):
    car = models.ForeignKey('autos.Car', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.car.brand + ' ' + self.car.model


class Car:
    pass

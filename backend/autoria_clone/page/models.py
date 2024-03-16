from django.db import models

class CarBrand(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class CarModel(models.Model):
    brand = models.ForeignKey(CarBrand, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class CarPrice(models.Model):
    car = models.ForeignKey(CarModel, on_delete=models.CASCADE)
    currency = models.CharField(max_length=3)
    price = models.DecimalField(max_digits=10, decimal_places=2)

class User(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField()
    account_type = models.CharField(max_length=100)

    def __str__(self):
        return self.username

class Ad(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    car = models.ForeignKey(CarModel, on_delete=models.CASCADE)
    price = models.ForeignKey(CarPrice, on_delete=models.CASCADE)
    content = models.TextField()

    def __str__(self):
        return f"Ad for {self.car} by {self.user}"


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
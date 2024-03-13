from django.db import models

class CarBrand(models.Model):
    name = models.CharField(max_length=100)

class CarModel(models.Model):
    brand = models.ForeignKey(CarBrand, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

class CarPrice(models.Model):
    car = models.ForeignKey(CarModel, on_delete=models.CASCADE)
    currency = models.CharField(max_length=3)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    date_updated = models.DateTimeField(auto_now=True)

class User(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField()
    account_type = models.CharField(max_length=10, choices=[('Basic', 'Basic'), ('Premium', 'Premium')])

class Ad(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    car = models.ForeignKey(CarModel, on_delete=models.CASCADE)
    price = models.ForeignKey(CarPrice, on_delete=models.CASCADE)
    content = models.TextField()
    is_active = models.BooleanField(default=False)
    is_edited = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)

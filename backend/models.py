from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    is_customer = models.BooleanField(default=True)
    is_seller = models.BooleanField(default=False)
    is_manager = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    advertisements_count = models.PositiveIntegerField(default=0)

class CarBrand(models.Model):
    name = models.CharField(max_length=100)

class CarModel(models.Model):
    objects = None
    brand = models.ForeignKey(CarBrand, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

class Advertisement(models.Model):
    objects = None
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    brand = models.ForeignKey(CarBrand, on_delete=models.CASCADE)
    model = models.ForeignKey(CarModel, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=3, choices=[('USD', 'USD'), ('EUR', 'EUR'), ('UAH', 'UAH')])
    status = models.CharField(max_length=10, choices=[('active', 'Active'), ('inactive', 'Inactive')])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def is_basic_account(self, LIMIT_BASIC_ACCOUNT=None):
        return self.user.advertisements_count < LIMIT_BASIC_ACCOUNT

def create_advertisement(user, LIMIT_BASIC_ACCOUNT=None, **kwargs):
    if user.is_basic_account():
        if user.advertisements_count >= LIMIT_BASIC_ACCOUNT:
            raise Exception("Too many advertisements for basic account.")
        user.advertisements_count += 1
        user.save()
    # створення оголошення
    advertisement = Advertisement(
        user=user,
        brand=kwargs['brand'],
        model=kwargs['model'],
        price=kwargs['price'],
        currency=kwargs['currency'],
        status='active'
    )
    advertisement.save()
    return advertisement

class PremiumAccount(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    purchase_date = models.DateTimeField(auto_now_add=True)

class PremiumAccount(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    purchase_date = models.DateTimeField(auto_now_add=True)

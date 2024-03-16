from django.db import models
from django.conf import settings

class Listing(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=3, choices=settings.CURRENCY_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_price_in_usd(self):
        exchange_rate = self.get_exchange_rate()
        return self.price * exchange_rate

    def get_exchange_rate(self, exchange_rate=None):
        

        return exchange_rate
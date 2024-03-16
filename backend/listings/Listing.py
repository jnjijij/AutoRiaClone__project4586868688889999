from django.db import models
from django.conf import settings
from django.core.exceptions import ValidationError

class Listing(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=3, choices=settings.CURRENCY_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def clean(self):
        #Check for inappropriate language
        inappropriate_words = ['badword1', 'badword2', 'badword3']
        if any(word in self.title.lower() for word in inappropriate_words):
            raise ValidationError('Title contains inappropriate language')
        if any(word in self.description.lower() for word in inappropriate_words):
            raise ValidationError('Description contains inappropriate language')

    def get_price_in_usd(self):
        exchange_rate = self.get_exchange_rate()
        return self.price * exchange_rate

    def get_exchange_rate(self, exchange_rate=None):
        # Get the exchange rate from the National Bank of Ukraine
        # ...
        return exchange_rate
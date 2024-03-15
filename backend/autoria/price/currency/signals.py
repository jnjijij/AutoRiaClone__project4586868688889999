from django.db.models.signals import post_save
from django.dispatch import receiver
from ..models import Currency

@receiver(post_save, sender=Currency)
def update_exchange_rate(created):
    if created:
        # Update the exchange rate based on the new currency
        pass
from django.db.models.signals import post_save
from django.dispatch import receiver

from backend.autoria.autos.models import Advertisement


class Money:
    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency


@receiver(post_save, sender=Advertisement)
def update_advertisement_price(instance, created, exchange_rate=None):
    if created or instance.price.currency != 'UAH':
        instance.price = Money(instance.price.amount * exchange_rate if exchange_rate else 1, 'UAH')
        instance.save()
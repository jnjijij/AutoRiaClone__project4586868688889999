from logging import Manager

from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Advertisement
from .models import Autosaloon
from ..advertisements.signals import Money


@receiver(post_save, sender=Autosaloon)
def create_autosaloon_manager(instance, created):
    if created:
        Manager.objects.create(autosaloon=instance)


@receiver(post_save, sender=Advertisement)
def update_advertisement_price(instance, created, exchange_rate=None, **kwargs):
    if created or instance.price.currency != 'UAH':
        instance.price = Money(instance.price.amount * exchange_rate, 'UAH')
        instance.save()

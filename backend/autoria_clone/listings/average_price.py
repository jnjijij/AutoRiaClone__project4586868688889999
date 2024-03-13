from django.db import models
from django.db.models import Avg


def calculate_average_price(region=None):
    if region:
        average_price = Listing.objects.filter(region=region).aggregate(avg_price=Avg('price'))['avg_price']
    else:
        average_price = Listing.objects.all().aggregate(avg_price=Avg('price'))['avg_price']
    return average_price


class Listing(models.Model):
    objects = None

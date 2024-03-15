from django.db import models

class Advertisement(models.Model):
    objects = None
    price = models.DecimalField(max_digits=10, decimal_places=2)
    # ...
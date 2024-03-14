from django.db import models

class Auto(models.Model):
    objects = None
    title = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=3)

    def __str__(self):
        return self.title
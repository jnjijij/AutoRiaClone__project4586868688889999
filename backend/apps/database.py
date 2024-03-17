# database.py
from django.db import models
from django.utils import timezone

class User(models.Model):
    username = models.CharField(max_length=80, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(default=timezone.now)

class Car(models.Model):
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    year = models.IntegerField()
    price = models.FloatField()
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)

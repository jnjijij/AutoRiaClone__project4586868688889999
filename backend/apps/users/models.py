from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import Group
from backend.core import db


class CustomUser(AbstractUser):
    phone = models.CharField(max_length=15)

    def __str__(self):
        return self.username


class UserMixin:
    pass


class User(UserMixin, db.Model):
    # ...
    query = None
    role = db.Column(default="customer", server_default="customer", index=True, )
    # ...


ROLE_USER = "user"
ROLE_MANAGER = "manager"
ROLE_ADMIN = "admin"


class AbstractUser(AbstractUser):
    ROLE_CHOICES = [
        ('C', 'Customer'),
        ('P', 'Provider'),
        ('M', 'Manager'),
        ('A', 'Administrator'),
    ]
    role = models.CharField(max_length=1, choices=ROLE_CHOICES, default='C')


class UserRole(models.Model):
    name = models.CharField(max_length=50)


class SalesRole(UserRole):
    objects = None


class MechanicRole(UserRole):
    objects = None


class PartnerRole(UserRole):
    objects = None


Group.objects.create(name='Basic')
Group.objects.create(name='Premium')

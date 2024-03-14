from django.contrib.auth.models import AbstractUser
from django.db import models

from backend.apps.core import db


class CustomUser(AbstractUser):
    phone = models.CharField(max_length=15)

    def __str__(self):
        return self.username


class UserMixin:
    pass


class User(UserMixin, db.Model):
    # ...
    query = None
    role = db.Column(default="customer", server_default="customer", index=True,)
    # ...


ROLE_USER = "user"
ROLE_MANAGER = "manager"
ROLE_ADMIN = "admin"

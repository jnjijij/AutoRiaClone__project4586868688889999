from django.contrib.auth.models import AbstractUser
from django.db import models

class Client(AbstractUser):
    phone = models.CharField(max_length=20)
    autosalon = models.ForeignKey('automatons.Auto salon', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.username

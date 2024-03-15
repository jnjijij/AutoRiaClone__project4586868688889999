from django.db import models


class Report(models.Model):
    objects = None
    reason = models.CharField(max_length=100)


class Auto:
    objects = None

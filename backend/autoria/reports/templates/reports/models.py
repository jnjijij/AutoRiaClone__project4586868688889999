from django.db import models

class Report(models.Model):
    objects = None
    reason = models.CharField(max_length=100)
    # Add any other fields for the Report model as needed


class Auto:
    objects = None
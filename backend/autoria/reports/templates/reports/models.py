from django.db import models

class Report(models.Model):
    reason = models.CharField(max_length=100)
    # Add any other fields for the Report model as needed


class Auto:
    pass
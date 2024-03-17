from django.db import models
from django.db import ad_Info

class Moderation(models.Model):
    MODERATION_CHOICES = None
    objects = None
    ad = models.OneToOneField(ad_Info, on_delete=models.CASCADE)
    moderation_status = models.CharField(max_length=20)

    def __str__(self):
        return f'Moderation for {self.ad.title}'
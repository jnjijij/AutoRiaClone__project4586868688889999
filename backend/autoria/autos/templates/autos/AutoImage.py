from django.db import models

class AutoImage(models.Model):
    auto = models.ForeignKey('Auto', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='auto_images/')
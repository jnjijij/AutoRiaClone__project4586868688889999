from django.db import models

class Auto(models.Model):
    objects = None
    title = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=3)
    images = models.ManyToManyField('Image', blank=True)

    def __str__(self):
        return self.title

class Image(models.Model):
    objects = None
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.image.name
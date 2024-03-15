from .models import Advertisement

def create_advertisement():
    advertisement = Advertisement.objects.create(price=100.00)
    advertisement.save()
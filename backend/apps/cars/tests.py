import pytest
from .models import CarListing

@pytest.mark.django_db
def test_car_listing_creation():
    car_listing = CarListing.objects.create(make='Toyota', model='Corolla', price=20000, currency='USD')
    assert car_listing.make == 'Toyota'
    assert car_listing.model == 'Corolla'
    assert car_listing.price == 20000
    assert car_listing.currency == 'USD'
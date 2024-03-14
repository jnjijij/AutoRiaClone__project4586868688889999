from django.contrib.auth import get_user_model
from django.db import models
from django.db.models import Avg, Sum
from django.utils import timezone

from backend.apps.core import db


class CarMake(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class CarModel(models.Model):
    make = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.make} - {self.name}"


def calculate_average_price(region=None):
    queryset = Listing.objects
    if region:
        queryset = queryset.filter(region=region)
    average_price = queryset.aggregate(avg_price=Avg('price'))['avg_price']
    return average_price


class Listing(models.Model):
    objects = None
    seller = models.ForeignKey('accounts.CustomUser', on_delete=models.CASCADE)
    make = models.ForeignKey(CarMake, on_delete=models.CASCADE)  # Changed to CarMake
    model = models.ForeignKey(CarModel, on_delete=models.CASCADE)  # Changed to CarModel
    price = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=3, choices=[('USD', 'USD'), ('EUR', 'EUR'), ('UAH', 'UAH')])
    views = models.PositiveIntegerField(default=0)
    region = models.CharField(max_length=100)
    views = models.PositiveIntegerField(default=0)
    views_today = models.PositiveIntegerField(default=0)
    views_this_week = models.PositiveIntegerField(default=0)
    views_this_month = models.PositiveIntegerField(default=0)
    average_price_region = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    average_price_city = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    average_price_country = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def track_view(self):
        self.views += 1
        self.save()


class SellerProfile(models.Model):
    user = models.OneToOneField('accounts.CustomUser', on_delete=models.CASCADE)
    account_type = models.CharField(max_length=10, choices=[('basic', 'Basic'), ('premium', 'Premium')])

    def get_views_per_period(self, period):
        if period == 'day':
            start_date = timezone.now() - timezone.timedelta(days=1)
        elif period == 'week':
            start_date = timezone.now() - timezone.timedelta(weeks=1)
        elif period == 'month':
            start_date = timezone.now() - timezone.timedelta(weeks=4)
        else:
            start_date = timezone.now() - timezone.timedelta(days=1)  # Default to day
        views = \
            Listing.objects.filter(seller=self.user, created_at__gte=start_date).aggregate(total_views=Sum('views'))[
                'total_views']
        return views


class Currency(models.Model):
    name = models.CharField(max_length=3)
    # Add fields for exchange rate and last updated date


class CarListing(models.Model):
    seller = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    make = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    model = models.ForeignKey(CarModel, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=(('active', 'Active'), ('inactive', 'Inactive')), default='active')


class HttpResponseForbidden:
    pass


class Region(db.Model):
    id = db.Column()
    name = db.Column()

    def __repr__(self):
        return f"<Region {self.name}>"


class Listing(db.Model):
    region_id = db.Column()
    region = db.relationship('Region', backref=db.backref('listings', lazy=True))

    class Listing(db.Model):
        # ...

        region_id = db.Column(db.Integer, db.ForeignKey('region.id'), nullable=False)
        region = db.relationship('Region', backref=db.backref('listings', lazy=True))

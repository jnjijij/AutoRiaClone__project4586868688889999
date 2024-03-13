from django.contrib.admindocs.utils import ROLES
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import Sum
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

from backend.listings.models import Listing


class CustomUser(AbstractUser):
    is_premium = models.BooleanField(default=False)


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


class User(AbstractUser):
    role = models.CharField(_('role'), max_length=20, choices=ROLES, default='buyer')
    account_type = models.CharField(_('account type'), max_length=10,
                                    choices=(('basic', 'Basic'), ('premium', 'Premium')), default='basic')

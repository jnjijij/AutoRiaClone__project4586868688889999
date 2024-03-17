import re

from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.core.exceptions import ValidationError
from django.db import models
from django.db.models import Avg, Count, Q, Sum
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from backend.models import Advertisement

# Визначення ролей
ROLES = (
    ('admin', 'Admin'),
    ('manager', 'Manager'),
    ('seller', 'Seller'),
    ('buyer', 'Buyer'),
)

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        # Логіка створення звичайного користувача
        pass

    def create_superuser(self, email, password, **extra_fields):
        # Логіка створення суперкористувача (адміністратора)
        pass

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=20, choices=ROLES, default='buyer')
    account_type = models.CharField(_('account type'), max_length=10,
                                    choices=(('basic', 'Basic'), ('premium', 'Premium')), default='basic')
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['role']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        # Логіка перевірки дозволів користувача
        pass

    def has_module_perms(self, app_label):
        # Логіка перевірки дозволів на модуль
        pass

class PremiumUser(models.Model):
    objects = None
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='premium_user')


class PremiumUserManager:
    pass


class Listing(models.Model):
    seller = models.ForeignKey(User, on_delete=models.CASCADE, related_name='listings')
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=3, choices=(('USD', 'USD'), ('EUR', 'EUR'), ('UAH', 'UAH')))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    views = models.PositiveIntegerField(default=0)

    objects = models.Manager()
    premium_objects = PremiumUserManager()

    def clean(self):
        # Перевірка на нецензурну лексику
        profanity_pattern = re.compile(r'\b(bad_word1|bad_word2|...)\b', re.IGNORECASE)
        if profanity_pattern.search(self.title) or profanity_pattern.search(self.description):
            raise ValidationError(_('Listing contains profanity.'))

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

class PremiumUserManager(models.Manager):
    def get_average_price(self, user, region=None):
        filters = Q(seller__premium_user__user=user)
        if region:
            filters &= Q(seller__region=region)
        return self.filter(filters).aggregate(avg_price=Avg('price'))['avg_price']

    def get_average_price_nationwide(self, user):
        return self.filter(seller__premium_user__user=user).aggregate(avg_price=Avg('price'))['avg_price']

    def get_listing_stats(self, user, period):
        if period == 'day':
            start_date = timezone.now() - timezone.timedelta(days=1)
        elif period == 'week':
            start_date = timezone.now() - timezone.timedelta(weeks=1)
        elif period == 'month':
            start_date = timezone.now() - timezone.timedelta(weeks=4)
        else:
            start_date = timezone.now() - timezone.timedelta(days=1)

        filters = Q(seller__premium_user__user=user, created_at__gte=start_date)
        return self.filter(filters).aggregate(total_views=Sum('views'), listing_count=Count('id'))



class PremiumAccount(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    expires_at = models.DateTimeField()
    price = models.DecimalField(max_digits=100, decimal_places=2)


class Purchase(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    premium_account = models.OneToOneField(PremiumAccount, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


class Account(models.Model):
    TYPES = (
        ('basic'),
        ('premium'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=10, choices=TYPES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
class PremiumAccount(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    purchase_date = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    premium_account = models.OneToOneField()
class Statistic(models.Model):
    advertisement = models.ForeignKey(Advertisement, on_delete=models.CASCADE)
    views_total = models.IntegerField(default=0)
    views_daily = models.IntegerField(default=0)
    views_weekly = models.IntegerField(default=0)
    views_monthly = models.IntegerField(default=0)
    average_price_region = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    average_price_ukraine = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def update_views(self):
        self.views_total += 1
        self.save()

    def update_daily_views(self):
        self.views_daily += 1
        self.save()

    def update_weekly_views(self):
        self.views_weekly += 1
        self.save()

    def update_monthly_views(self):
        self.views_monthly += 1
        self.save()

    def update_average_price(self):
        region = self.advertisement.region
        self.average_price_region = Advertisement.objects.filter(region=region).aggregate(Avg('price'))['price__avg']
        self.average_price_ukraine = Advertisement.objects.aggregate(Avg('price'))['price__avg']
        self.save()

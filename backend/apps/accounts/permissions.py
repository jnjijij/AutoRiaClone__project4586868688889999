import re

import sender
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin, Permission
from django.contrib.contenttypes.models import ContentType
from django.core.exceptions import ValidationError
from django.db import models
from django.db.models import Avg, Count, Q, Sum
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from backend.apps.accounts.models import PremiumUserManager

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
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='premium_user')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        view_stats_permission = Permission.objects.get(codename='view_statistics')
        self.user.user_permissions.add(view_stats_permission)

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

class Permissions:
    @staticmethod
    def add_custom_permissions():
        content_type = ContentType.objects.get_for_model(User)
        Permission.objects.create(content_type=content_type, codename='view_statistics', name='Can view listing statistics')

def create_custom_permissions(sender, **kwargs):
    if kwargs.get('created', False):
        Permissions.add_custom_permissions()

models.signals.post_migrate.connect(create_custom_permissions, sender=sender)

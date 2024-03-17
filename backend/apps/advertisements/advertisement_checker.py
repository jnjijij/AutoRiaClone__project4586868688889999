from datetime import timezone, timedelta

from django.contrib.auth import get_user_model
from .models import Advertisement, AdvertisementStatistics
from ...configs import models


def check_for_obscene_words(text):
    # реалізація перевірки тексту на неприйнятну лексику
    pass

def check_advertisements():
    User = get_user_model()
    for advertisement in Advertisement.objects.all():
        if not check_for_obscene_words(advertisement.description):
            advertisement.status = 'inactive'
            advertisement.save()
            send_notification_to_manager(advertisement.seller.user)

def send_notification_to_manager(user):
    # реалізація відправлення повідомлення менеджеру
    pass

def update_advertisement_statistics():
    for advertisement in Advertisement.objects.all():
        statistics = AdvertisementStatistics.objects.get_or_create(advertisement=advertisement)[0]
        statistics.views += 1
        statistics.save()

def update_daily_weekly_monthly_views():
    for advertisement_statistics in AdvertisementStatistics.objects.all():
        today = timezone.now().date()
        daily_views = advertisement_statistics.views_set.filter(date=today).count()
        weekly_views = advertisement_statistics.views_set.filter(date__gte=today - timedelta(days=7)).count()
        monthly_views = advertisement_statistics.views_set.filter(date__gte=today - timedelta(days=30)).count()
        advertisement_statistics.daily_views = daily_views
        advertisement_statistics.weekly_views = weekly_views
        advertisement_statistics.monthly_views = monthly_views
        advertisement_statistics.save()

class AdvertisementView(models.Model):
    advertisement = models.ForeignKey(Advertisement, on_delete=models.CASCADE)
    date = models.DateField(default=timezone.now)
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import PremiumUser, User


@receiver(post_save, sender=User)
def upgrade_user_to_premium(instance, created):
    if created or instance.is_premium:
        PremiumUser.objects.create(user=instance)
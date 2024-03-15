from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import User


class Role:
    objects = None


@receiver(post_save, sender=User)
def create_user_role(instance, created):
    if created:
        Role.objects.create(user=instance, name='POKUPATEL')
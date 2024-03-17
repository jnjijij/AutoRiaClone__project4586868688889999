from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail

from .models import Consumer

@receiver(post_save, sender=Consumer)
def send_new_consumer_email(instance, created):
    if created:
        subject = f"New Consumer: {instance.first_name} {instance.last_name}"
        message = f"A new consumer has been created:\n\n{instance.email}\n{instance.phone_number}"
        send_mail(
            subject=subject,
            message=message,
            from_email="your_email@example.com",
            recipient_list=["recipient@example.com"],
            fail_silently=False,
        )
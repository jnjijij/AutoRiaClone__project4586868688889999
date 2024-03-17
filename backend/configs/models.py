from backend.core import models
from backend.database import User


class Notification(models.Model):
    objects = None
    user = models.ForeignKey()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class NotificationManager:
    @staticmethod
    def send_notification(user, message):
        Notification.objects.create(user=user, message=message)


class ForeignKey:
    pass


class TextField:
    pass


class Model:
    pass


class DateTimeField:
    pass


class CharField:
    pass


class DecimalField:
    pass


class DateField:
    pass
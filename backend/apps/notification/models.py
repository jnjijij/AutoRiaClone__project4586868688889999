from backend.configs import models



class Notification(models.Model):
    objects = None
    user = models.ForeignKey()
    message = models.TextField()
    created_at = models.DateTimeField()

class NotificationManager:
    @staticmethod
    def send_notification(user, message):
        Notification.objects.create(user=user, message=message)
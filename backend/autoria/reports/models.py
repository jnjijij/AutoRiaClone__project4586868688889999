from models import Auto
from django.db.models import models


class Report(models.Model):
    AUTO_STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('resolved', 'Resolved'),
        ('dismissed', 'Dismissed'),
    )

    auto = models.ForeignKey(Auto, on_delete=models.CASCADE)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    reason = models.CharField(max_length=255)
    status = models.CharField(max_length=10, choices=AUTO_STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user} reported {self.auto}'


class Auto:
    pass


class AutoImage:
    pass
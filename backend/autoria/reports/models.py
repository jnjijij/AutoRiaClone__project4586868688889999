from django.db.models import Model, CharField, IntegerField, DateField, TextField, ForeignKey, CASCADE
from autos.models import Auto

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

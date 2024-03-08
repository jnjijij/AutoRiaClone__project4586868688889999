from django.db import models
from django.contrib.auth.models import User

class Auto(models.Model):
    name = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=3, choices=(('USD', 'USD'), ('EUR', 'EUR'), ('UAH', 'UAH')))
    description = models.TextField()
    image = models.ImageField(upload_to='autos/')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name} {self.model}'

class Autosalon(models.Model):
    name = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class AutoImage(models.Model):
    auto = models.ForeignKey(Auto, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='autos/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.auto} image'

class Report(models.Model):
    auto = models.ForeignKey(Auto, on_delete=models.CASCADE, related_name='reports')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reports')
    reason = models.CharField(max_length=255)
    resolved = models.BooleanField(default=False)
    dismissed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} reported {self.auto}'

class Auto(models.Model):
    # ...
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Image(models.Model):
    auto = models.ForeignKey(Auto, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')

class Advertisement(models.Model):


 class Report(models.Model):
     class ReportViewHistory(models.Model):
         id = models.AutoField(primary_key=True)
         user = models.ForeignKey(User, on_delete=models.CASCADE)
         viewed_report = models.ForeignKey(Report, on_delete=models.CASCADE)
         date_created = models.DateTimeField(auto_now_add=True)

         def __str__(self):
             return f'{self.user.username} переглянув звіт {self.viewed_report.title} ({self.date_created})'


class Course(models.Model):
    class ReportViewHistory(models.Model):
     id = models.AutoField(primary_key=True)
     user = models.ForeignKey(User, on_delete=models.CASCADE)
     viewed_report = models.ForeignKey(Report, on_delete=models.CASCADE)
     date_created = models.DateTimeField(auto_now_add=True)

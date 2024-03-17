from django.db.models import Count, models
from django.db.models.functions import TruncMonth, TruncWeek, TruncDay
from django.shortcuts import render, redirect
from .models import AdInfo
from .forms import AdInfoForm
from ...database import User
from ...listings.models import Ad


def ad_list(request):
    ads = AdInfo.objects.all()
    return render(request, 'ad_info/ad_list.html', {'ads': ads})

def ad_detail(request, pk):
    ad = AdInfo.objects.get(pk=pk)
    return render(request, 'ad_info/ad_detail.html', {'ad': ad})

def ad_create(request):
    if request.method == 'POST':
        form = AdInfoForm(request.POST, request.FILES)
        if form.is_valid():
            ad = form.save()
            return redirect('ad_detail', pk=ad.pk)
    else:
        form = AdInfoForm()
    return render(request, 'ad_info/ad_create.html', {'form': form})

class View(models.Model):
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

class Views:
    @staticmethod
    def get_views(ad):
        return View.objects.filter(ad=ad)

    @staticmethod
    def get_views_per_day(ad):
        return View.objects.filter(ad=ad).values_list('created_at', flat=True).annotate(day=TruncDay('created_at')).values('day').annotate(count=Count('id'))

    @staticmethod
    def get_views_per_week(ad):
        return View.objects.filter(ad=ad).values_list('created_at', flat=True).annotate(week=TruncWeek('created_at')).values('week').annotate(count=Count('id'))

    @staticmethod
    def get_views_per_month(ad):
        return View.objects.filter(ad=ad).values_list('created_at', flat=True).annotate(month=TruncMonth('created_at')).values('month').annotate(count=Count('id'))
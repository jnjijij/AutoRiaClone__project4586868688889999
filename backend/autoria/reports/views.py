from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views import View

from .models import Report, Auto
from django.shortcuts import render, redirect
from .models import AutoImage
from .forms import AutoImageForm
from django.shortcuts import render
from .models import Auto

class ReportListView(View):
    @login_required(login_url=reverse_lazy('accounts:login'))
    def get(self, request):
        auto_id = request.user.auto.pk
        reports = Report.objects.filter(auto=auto_id, status='pending')
        return render(request, 'reports/report_list.html', {'reports': reports})

class ReportDetailView(View):
    @login_required(login_url=reverse_lazy('accounts:login'))
    def get(self, request, *args, **kwargs):
        report = get_object_or_404(Report, pk=kwargs['report_id'])
        return render(request, 'reports/report_detail.html', {'report': report})

class ReportDismissView(View):
    @login_required(login_url=reverse_lazy('accounts:login'))
    def post(self, request, *args, **kwargs):
        report = get_object_or_404(Report, pk=kwargs['report_id'])
        report.status = 'dismissed'
        report.save()
        auto = Auto.objects.get(pk=report.auto.pk)
        return redirect('reports:report_list', auto_id=auto.pk)

class ReportDeleteAllView(View):
    @login_required(login_url=reverse_lazy('accounts:login'))
    def post(self, request, *args, **kwargs):
        auto = Auto.objects.get(pk=kwargs['auto_id'])
        report_list = Report.objects.filter(auto=auto.pk, status='pending')
        for report in report_list:
            report.delete()
        return redirect('reports:report_list', auto_id=auto.pk)


def auto_image_update(request, auto_pk, image_pk):
    auto_image = AutoImage.objects.get(pk=image_pk)
    if request.method == 'POST':
        form = AutoImageForm(request.POST, request.FILES, instance=auto_image)
        if form.is_valid():
            form.save()
            return redirect('auto_images')
    else:
        form = AutoImageForm(instance=auto_image)
    return render(request, 'auto_image_update.html', {'form': form})

def auto_image_delete(request, auto_pk, image_pk):
    auto_image = AutoImage.objects.get(pk=image_pk)
    if request.method == 'POST':
        auto_image.delete()
        return redirect('auto_images')
    else:
        return render(request, 'auto_image_delete.html', {'auto_image': auto_image})

def report(request):
    autos = Auto.objects.all()
    return render(request, 'reports/report.html', {'autos': autos})


class ReportCreateView:
    @classmethod
    def as_view(cls):
        pass


class ReportResolveView:
    @classmethod
    def as_view(cls):
        pass
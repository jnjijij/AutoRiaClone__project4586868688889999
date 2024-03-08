from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from .models import Report, Auto

@login_required(login_url=reverse_lazy('accounts:login'))
def report_list(request):
    auto_id = request.user.auto.pk
    reports = Report.objects.filter(auto=auto_id, status='pending')
    return render(request, 'reports/report_list.html', {'reports': reports})

@login_required(login_url=reverse_lazy('accounts:login'))
def report_detail(request, report_id):
    report = get_object_or_404(Report, pk=report_id)
    return render(request, 'reports/report_detail.html', {'report': report})

@login_required(login_url=reverse_lazy('accounts:login'))
def report_dismiss(request, report_id):
    report = get_object_or_404(Report, pk=report_id)
    report.status = 'dismissed'
    report.save()
    auto = Auto.objects.get(pk=report.auto.pk)
    return redirect('reports:report_list', auto_id=auto.pk)

@login_required(login_url=reverse_lazy('accounts:login'))
def report_delete_all(request, auto_id):
    auto = Auto.objects.get(pk=auto_id)
    report_list = Report.objects.filter(auto=auto.pk, status='pending')
    for report in report_list:
        report.delete()
    return redirect('reports:report_list', auto_id=auto.pk)
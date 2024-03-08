# reports/views.py
from django.shortcuts import render, redirect
from .models import Report
from .forms import ReportForm

def report_list(request):
    reports = Report.objects.all()
    return render(request, 'reports/report_list.html', {'reports': reports})

def report_create(request):
    if request.method == 'POST':
        form = ReportForm(request.POST)
        if form.is_valid():
            report = form.save(commit=False)
            report.save()
            return redirect('report_detail', pk=report.pk)
    else:
        form = ReportForm()
    return render(request, 'reports/report_form.html', {'form': form})

def report_detail(request, pk):
    report = Report.objects.get(pk=pk)
    return render(request, 'reports/report_detail.html', {'report': report})

def report_update(request, pk):
    report = Report.objects.get(pk=pk)
    if request.method == 'POST':
        form = ReportForm(request.POST, instance=report)
        if form.is_valid():
            report = form.save(commit=False)
            report.save()
            return redirect('report_detail', pk=report.pk)
    else:
        form = ReportForm(instance=report)
    return render(request, 'reports/report_form.html', {'form': form})

def report_delete(request, pk):
    report = Report.objects.get(pk=pk)
    report.delete()
    return redirect('report_list')

def report_confirm_delete(request, pk):
    report = Report.objects.get(pk=pk)
    return render(request, 'reports/report_confirm_delete.html', {'report': report})
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from .models import Report, Auto

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
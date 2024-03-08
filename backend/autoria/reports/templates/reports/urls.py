from django.urls import path
from . import views

urlpatterns = [
    path(r'^$', views.ReportListView.as_view(), name='report_list'),
    path(r'^(?P<report_id>[0-9]+)/$', views.ReportDetailView.as_view(), name='report_detail'),
    path(r'^dismiss/(?P<report_id>[0-9]+)/$', views.ReportDismissView.as_view(), name='report_dismiss'),
    path(r'^delete_all/(?P<auto_id>[0-9]+)/$', views.ReportDeleteAllView.as_view(), name='report_delete_all'),
]
from django.urls import path
from . import views

app_name = 'reports'
urlpatterns = [
    path('', views.ReportListView.as_view(), name='report_list'),
    path('create/', views.ReportCreateView.as_view(), name='report_create'),
    path('<int:report_id>/', views.ReportDetailView.as_view(), name='report_detail'),
    path('<int:report_id>/resolve/', views.ReportResolveView.as_view(), name='report_resolve'),
    path('<int:report_id>/dismiss/', views.ReportDismissView.as_view(), name='report_dismiss'),
    path('<int:auto_id>/delete_all/', views.ReportDeleteAllView.as_view(), name='report_delete_all'),
]
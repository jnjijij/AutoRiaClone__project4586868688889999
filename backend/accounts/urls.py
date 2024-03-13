from django.urls import path
import views

urlpatterns = [
    path('manage-users/', views.manage_users, name='manage_users'),
    path('upgrade-account/', views.upgrade_account, name='upgrade_account'),
    path('view-statistics/', views.view_statistics, name='view_statistics'),
]

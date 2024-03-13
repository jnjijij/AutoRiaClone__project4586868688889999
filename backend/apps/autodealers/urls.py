from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='dealer_index'),
    path('<int:dealer_id>/', views.detail, name='dealer_detail'),
    path('create/', views.create, name='dealer_create'),
    path('<int:dealer_id>/update/', views.update, name='dealer_update'),
    path('<int:dealer_id>/delete/', views.delete, name='dealer_delete'),
    path('autosalons/', views.autosalon_list, name='auto salon_list'),
    path('clients/', views.client_list, name='client_list'),
    path('autosalons/', views.autosalon_list, name='auto salon_list'),
    path('autosalons/<int:pk>/', views.autosalon_detail, name='auto salon_detail'),
    path('clients/', views.client_list, name='client_list'),
    path('clients/<int:pk>/', views.client_detail, name='client_detail'),
]

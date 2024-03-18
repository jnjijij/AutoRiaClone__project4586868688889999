# backend/autoria/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('cars/', views.car_list, name='car_list'),
]

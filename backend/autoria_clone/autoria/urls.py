from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add_auto/', views.add_auto, name='add_auto'),
    path('auto_images/<int:auto_id>/', views.auto_images, name='auto_images'),
]
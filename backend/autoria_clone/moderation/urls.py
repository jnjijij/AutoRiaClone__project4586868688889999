from django.urls import path
from . import views

urlpatterns = [
    path('', views.moderation_list, name='moderation_list'),
    path('<int:pk>/', views.moderation_detail, name='moderation_detail'),
    path('<int:ad_pk>/create/', views.moderation_create, name='moderation_create'),
]
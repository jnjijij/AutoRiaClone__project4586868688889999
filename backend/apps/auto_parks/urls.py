from django.urls import path
from . import views

urlpatterns = [
    path('parks/', views.ParkListCreate.as_view(), name='park-list-create'),
    path('parks/<int:pk>/', views.ParkRetrieveUpdateDestroy.as_view(), name='park-retrieve-update-destroy'),
    path('parks/search/', views.ParkSearch.as_view(), name='park-search'),
]
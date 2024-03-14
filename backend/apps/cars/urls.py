from django.urls import path
from views import CarListCreate

urlpatterns = [
    path('', CarListCreate.as_view(), name='car-list-create'),
]
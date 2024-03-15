from django.urls import path
from .views import create_advertisement

urlpatterns = [
    path('create_advertisement/', create_advertisement, name='create_advertisement'),
]
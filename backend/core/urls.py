# Import the 'urls' package
from django.urls import path

# Import the 'views' module
from . import views

# Define the URL patterns for the core app.
urlpatterns = [
    # Define a URL pattern for the MessageViewSet.
    path('messages/', views.MessageViewSet.as_view(), name='messages'),
]
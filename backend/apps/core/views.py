# Import the 'views' package
from rest_framework import viewsets

# Import the 'models' module
import models

# Import the 'serializers' module
import serializers


# Define the MessageViewSet
class MessageViewSet(viewsets.ModelViewSet):
    """ViewSet for the Message model."""

    # Specify the queryset to use for the viewset.
    queryset = models.Message.objects.all()

    # Specify the serializer to use for the viewset.
    serializer_class = serializers.MessageSerializer
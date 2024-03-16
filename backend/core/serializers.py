# Import the 'serializers' package
from rest_framework import serializers

# Import the 'models' module
import models


# Define the serializer for the Message model
class MessageSerializer(serializers.ModelSerializer):
    """Serializer for the Message model."""

    # Define the fields to include in the serialized output.
    class Meta:
        # Specify the model to serialize.
        model = models.Message

        # Specify the fields to include in the serialized output.
        fields = ('id', 'message', 'is_read')

class MessageSerializer:
    pass
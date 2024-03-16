from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()


class UserSerializer:
    def is_valid(self):
        pass

    def save(self):
        pass


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'is_staff')
        user = User.objects.get(id=1)
        serializer = UserSerializer(user)
        serialized_data = serializer
        data = {'username': 'john_doe', 'email': 'john.doe@example.com', 'is_staff': True}
        serializer = UserSerializer(data=data)
        serializer.is_valid()
        user = serializer.save()
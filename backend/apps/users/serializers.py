from rest_framework import serializers
from models import CustomUser

from backend.apps.users.models import UserRole


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'
class UserRoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserRole
        fields = '__all__'

class SalesRoleSerializer(UserRoleSerializer):
    pass

class MechanicRoleSerializer(UserRoleSerializer):
    pass

class PartnerRoleSerializer(UserRoleSerializer):
    pass
from rest_framework import generics, viewsets

from models import CustomUser
from serializers import CustomUserSerializer

from backend.apps.users.models import SalesRole, MechanicRole, PartnerRole


class CustomUserListCreate(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

class CustomUserRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


class SalesRoleSerializer:
    pass


class SalesRoleViewSet(viewsets.ModelViewSet):
    queryset = SalesRole.objects.all()
    serializer_class = SalesRoleSerializer


class MechanicRoleSerializer:
    pass


class MechanicRoleViewSet(viewsets.ModelViewSet):
    queryset = MechanicRole.objects.all()
    serializer_class = MechanicRoleSerializer


class PartnerRoleSerializer:
    pass


class PartnerRoleViewSet(viewsets.ModelViewSet):
    queryset = PartnerRole.objects.all()
    serializer_class = PartnerRoleSerializer
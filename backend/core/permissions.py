
from flask import Response
from rest_framework import permissions, status
from rest_framework.decorators import api_view, permission_classes

from backend.apps.auto_parks.models import CarPark
from backend.apps.auto_parks.serializers import CarParkSerializer


class IsAuthenticatedOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow authenticated users to view core details.
    """
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user and request.user.is_authenticated
@api_view(['GET'])
@permission_classes([IsAuthenticatedOrReadOnly])
def core_details(request, pk):
    try:
        car_park = CarPark.objects.get(pk=pk)
    except CarPark.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = CarParkSerializer(car_park)
    return Response(serializer.data)


class BasePermission:
    pass
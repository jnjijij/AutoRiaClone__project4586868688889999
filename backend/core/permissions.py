
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import BasePermission, IsAuthenticatedOrReadOnly

from backend.apps.auto_parks.models import CarPark
from backend.apps.auto_parks.serializers import CarParkSerializer

@api_view(['GET'])
@permission_classes([IsAuthenticatedOrReadOnly])
def core_details(request, pk):
    try:
        car_park: object = CarPark.objects.get(pk=pk)
    except CarPark.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = CarParkSerializer(car_park)
    return Response(serializer.data)
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from .models import CarPark
from .serializers import CarParkSerializer

# ...

@api_view(['GET'])
@permission_classes([IsAuthenticatedOrReadOnly])
def car_park_details(request, pk):
    try:
        car_park = CarPark.objects.get(pk=pk)
    except CarPark.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = CarParkSerializer(car_park)
    return Response(serializer.data)
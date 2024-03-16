from rest_framework import generics, permissions, pagination
from django.shortcuts import get_object_or_404
from .models import Park
from .serializers import ParkSerializer

class ParkListCreate(generics.ListCreateAPIView):
    queryset = Park.objects.all()
    serializer_class = ParkSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class ParkRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Park.objects.all()
    serializer_class = ParkSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        pk = self.kwargs['pk']
        park = get_object_or_404(Park, id=pk)
        return park

class ParkSearch(generics.ListAPIView):
    serializer_class = ParkSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            queryset = Park.objects.filter(name__icontains=query)
        else:
            queryset = Park.objects.none()
        return queryset

class ParkList(generics.ListAPIView):
    queryset = Park.objects.all()
    serializer_class = ParkSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = pagination.PageNumberPagination

class ParkListCreate:
    @classmethod
    def as_view(cls):
        pass


class ParkRetrieveUpdateDestroy:
    @classmethod
    def as_view(cls):
        pass


class ParkSearch:
    @classmethod
    def as_view(cls):
        pass
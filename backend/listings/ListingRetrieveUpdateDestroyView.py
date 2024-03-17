
from rest_framework import generics
from rest_framework.permissions import IsAdminUserOrReadOnlyForListings
from rest_framework.exceptions import PermissionDenied
from rest_framework.response import Response

from .models import Listing
from .serializers import ListingSerializer

class ListingRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer
    permission_classes = [IsAdminUserOrReadOnlyForListings]

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if instance.edits_left > 0:
            instance.edits_left -= 1
            instance.save()
        else:
           raise PermissionDenied('You have exceeded the maximum number of edits for this listing')

        return Response(serializer.data)

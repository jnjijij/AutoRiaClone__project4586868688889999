from rest_framework import generics
from rest_framework.permissions import IsAdminUserOrReadOnly
from .models import Listing
from .serializers import ListingSerializer
from ..configs import models


class ListingListCreateView(generics.ListCreateAPIView):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer
    permission_classes = [IsAdminUserOrReadOnly]

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.annotate(price_in_usd=models.ExpressionWrapper(models.F('price') * models.F('exchange_rate'),


       ))
        return queryset
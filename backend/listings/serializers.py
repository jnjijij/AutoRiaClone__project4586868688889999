from rest_framework import serializers
from .models import Listing

class ListingSerializer(serializers.ModelSerializer):
    price_in_usd = serializers.SerializerMethodField()

    class Meta:
        model = Listing
        fields = ['id', 'title', 'description', 'price', 'currency', 'created_at', 'updated_at', 'price_in_usd']

    def get_price_in_usd(self, obj):
        return obj.get_price_in_usd()
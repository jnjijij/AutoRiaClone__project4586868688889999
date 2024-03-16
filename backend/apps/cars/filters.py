from django_filters import rest_framework as filters

from apps.cars.models import CarModel

# CarModel.objects.filter(brand__icontains=)


class CarFilter(filters.FilterSet):
    year_lt = filters.NumberFilter('year', 'lt')
    year_gt = filters.NumberFilter('year', 'gt')
    brand = filters.CharFilter('brand', 'icontains')
    order = filters.OrderingFilter(
        fields=(
            'id',
            'brand',
            ('year', 'asd')
        )
    )
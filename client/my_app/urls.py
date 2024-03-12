from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CarBrandViewSet, CarModelViewSet, CarPriceViewSet

router = DefaultRouter()
router.register(r'car_brands', CarBrandViewSet)
router.register(r'car_models', CarModelViewSet)
router.register(r'car_prices', CarPriceViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

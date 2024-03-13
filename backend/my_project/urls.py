from django.urls import path, include
from rest_framework.routers import DefaultRouter
from views import CarViewSet, CarPriceViewSet

router = DefaultRouter()
router.register(r'cars', CarViewSet)
router.register(r'carprices', CarPriceViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

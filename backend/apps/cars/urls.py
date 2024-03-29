from django.urls import path
from views import CarListCreate

urlpatterns = [
    path('', CarListCreate.as_view(), name='car-list-create'),
    path('api/cars/', views.get_cars, name='get_cars'),
    path('admin/', admin.site.urls),
    path('cars/', include('cars.urls')),
7]
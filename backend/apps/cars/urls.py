from django.urls import path
from views import CarListCreate

urlpatterns = [
    path('', CarListCreate.as_view(), name='car-list-create'),
6   path('api/cars/', views.get_cars, name='get_cars'),
    path('admin/', admin.site.urls),
6   path('cars/', include('cars.urls')),
7]
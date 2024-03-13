from django.contrib import admin
from django.urls import path, include
from rest_framework.schemas import get_schema_view

schema_view = get_schema_view(title='API')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('accounts.urls')),
    path('api/', include('ads.urls')),
    path('api-auth/', include),
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
]

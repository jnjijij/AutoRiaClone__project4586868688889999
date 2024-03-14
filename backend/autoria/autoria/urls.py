import os

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from backend.config.settings import BASE_DIR

urlpatterns = [
    path('admin/', admin.site.urls),
    path('autos/', include('autos.urls', namespace='autos')),
    path('reports/', include('reports.urls', namespace='reports')),
]

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
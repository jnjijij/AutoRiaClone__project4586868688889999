from xml.etree.ElementInclude import include

from django.urls import path
from . import views
from ..autoria import admin

urlpatterns = [
    path('', views.ad_list, name='ad_list'),
    path('<int:pk>/', views.ad_detail, name='ad_detail'),
    path('create/', views.ad_create, name='ad_create'),
    path('admin/', admin.site.urls),
    path('ad_info/', include('Ad_info.urls')),
]

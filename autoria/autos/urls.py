from django.urls import path
from . import views

app_name = 'autos'
urlpatterns = [
    path('', views.auto_list, name='auto_list'),
    path('create/', views.auto_create, name='auto_create'),
    path('<int:pk>/', views.auto_detail, name='auto_detail'),
    path('<int:pk>/update/', views.auto_update, name='auto_update'),
    path('<int:pk>/delete/', views.auto_delete, name='auto_delete'),
    path('<int:pk>/delete/', views.AutoDeleteView.as_view(), name='auto_delete'),
]
urlpatterns = [
    # ...
    path('<int:auto_pk>/images/create/', views.auto_image_create, name='auto_image_create'),
    path('<int:auto_pk>/images/<int:image_pk>/update/', views.auto_image_update, name='auto_image_update'),
    path('<int:auto_pk>/images/<int:image_pk>/delete/', views.auto_image_delete, name='auto_image_delete'),
]
urlpatterns = [
    path('upload_auto_image/', views.upload_auto_image, name='upload_auto_image'),
    path('auto_images/', views.auto_images, name='auto_images'),
]
urlpatterns = [
    # your other url patterns
    path('<int:auto_pk>/images/<int:image_pk>/update/', views.auto_image_update, name='auto_image_update'),
    path('<int:auto_pk>/images/<int:image_pk>/delete/', views.auto_image_delete, name='auto_image_delete'),
]
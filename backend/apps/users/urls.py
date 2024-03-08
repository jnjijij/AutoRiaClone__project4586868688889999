from django.urls import path
from .views import CustomUserListCreate, CustomUserRetrieveUpdateDestroy

urlpatterns = [
    path('', CustomUserListCreate.as_view(), name='user-list-create'),
    path('<int:pk>/', CustomUserRetrieveUpdateDestroy.as_view(), name='user-retrieve-update-destroy'),
]
from django.urls import path
from .views import ListingListCreateView, ListingRetrieveUpdateDestroyView, UserListCreateView, UserRetrieveUpdateDestroyView, RoleListCreateView, RoleRetrieveUpdateDestroyView, AccountListCreateView, AccountRetrieveUpdateDestroyView

urlpatterns = [
    path('listings/', ListingListCreateView.as_view(), name='listing_list_create'),
    path('listings/<int:pk>/', ListingRetrieveUpdateDestroyView.as_view(), name='listing_retrieve_update_destroy'),
    path('users/', UserListCreateView.as_view(), name='user_list_create'),
    path('users/<int:pk>/', UserRetrieveUpdateDestroyView.as_view(), name='user_retrieve_update_destroy'),
    path('roles/', RoleListCreateView.as_view(), name='role_list_create'),
    path('roles/<int:pk>/', RoleRetrieveUpdateDestroyView.as_view(), name='role_retrieve_update_destroy'),
    path('accounts/', AccountListCreateView.as_view(), name='account_list_create'),
    path('accounts/<int:pk>/', AccountRetrieveUpdateDestroyView.as_view(), name='account_retrieve_update_destroy'),
]
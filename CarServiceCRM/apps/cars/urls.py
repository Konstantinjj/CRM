from django.urls import path
from .views import CarListView, CarCreateView, CarUpdateView, CarDeleteView

urlpatterns = [
    path('', CarListView.as_view(), name='car_list'),
    path('create/', CarCreateView.as_view(), name='car_create'),
    path('create/<int:client_id>/', CarCreateView.as_view(), name='car_create_for_client'),
    path('edit/<int:pk>/', CarUpdateView.as_view(), name='car_edit'),
    path('delete/<int:pk>/', CarDeleteView.as_view(), name='car_delete'),
]
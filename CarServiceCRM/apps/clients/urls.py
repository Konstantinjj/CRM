from django.urls import path
from .views import ClientListView, ClientCreateView, ClientUpdateView, ClientDeleteView, ClientCarsView, ClientDetailView

urlpatterns = [
    path('', ClientListView.as_view(), name='client_list'),
    path('create/', ClientCreateView.as_view(), name='client_create'),
    path('edit/<int:pk>/', ClientUpdateView.as_view(), name='client_edit'),
    path('delete/<int:pk>/', ClientDeleteView.as_view(), name='client_delete'),
    path('cars/<int:pk>/', ClientCarsView.as_view(), name='client_cars'),
    path('detail/<int:pk>/', ClientDetailView.as_view(), name='client_detail'),
]

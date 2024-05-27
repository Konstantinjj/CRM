from django.urls import path
from . import views

urlpatterns = [
    path('', views.item_list, name='item_list'),
    path('create/', views.item_create, name='item_create'),
    path('edit/<int:pk>/', views.item_edit, name='item_edit'),
    path('delete/<int:pk>/', views.item_delete, name='item_delete'),
]

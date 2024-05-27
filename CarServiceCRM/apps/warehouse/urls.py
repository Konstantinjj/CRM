from django.urls import path
from .views import ItemListView, ItemCreateView, ItemUpdateView, ItemDeleteView

urlpatterns = [
    path('', ItemListView.as_view(), name='item_list'),
    path('create/', ItemCreateView.as_view(), name='item_create'),
    path('edit/<int:pk>/', ItemUpdateView.as_view(), name='item_edit'),
    path('delete/<int:pk>/', ItemDeleteView.as_view(), name='item_delete'),
]

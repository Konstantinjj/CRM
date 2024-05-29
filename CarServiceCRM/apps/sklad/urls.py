from django.urls import path
from .views import OverviewListView, ItemCreateView, ItemUpdateView, ItemDeleteView

urlpatterns = [
    path('overview/', OverviewListView.as_view(), name='overview'),
    path('create/', ItemCreateView.as_view(), name='item_create'),
    path('edit/<int:pk>/', ItemUpdateView.as_view(), name='item_edit'),
    path('delete/<int:pk>/', ItemDeleteView.as_view(), name='item_delete'),
]

from django.urls import path
from .views import WorkTypeListView, WorkTypeCreateView, WorkTypeUpdateView, WorkTypeDeleteView

urlpatterns = [
    path('', WorkTypeListView.as_view(), name='worktype_list'),
    path('create/', WorkTypeCreateView.as_view(), name='worktype_create'),
    path('edit/<int:pk>/', WorkTypeUpdateView.as_view(), name='worktype_edit'),
    path('delete/<int:pk>/', WorkTypeDeleteView.as_view(), name='worktype_delete'),
]

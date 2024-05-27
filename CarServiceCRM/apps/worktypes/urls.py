from django.urls import path
from . import views

urlpatterns = [
    path('', views.worktype_list, name='worktype_list'),
    path('create/', views.worktype_create, name='worktype_create'),
    path('edit/<int:pk>/', views.worktype_edit, name='worktype_edit'),
    path('delete/<int:pk>/', views.worktype_delete, name='worktype_delete'),
]

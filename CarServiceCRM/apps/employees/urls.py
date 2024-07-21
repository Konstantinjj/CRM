from django.urls import path
from .views import EmployeeListView, EmployeeUpdateView

urlpatterns = [
    path('', EmployeeListView.as_view(), name='employee_list'),
    path('edit/<int:pk>/', EmployeeUpdateView.as_view(), name='employee_edit'),
]

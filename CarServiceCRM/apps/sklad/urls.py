from django.urls import path
from .views import OverviewListView

urlpatterns = [
    path('overview/', OverviewListView.as_view(), name='overview'),
]
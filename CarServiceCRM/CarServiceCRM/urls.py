from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('clients/', include('clients.urls')),
    path('cars/', include('cars.urls')),
    path('warehouse/', include('warehouse.urls')),
]

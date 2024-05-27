from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.main.urls')),
    path('clients/', include('apps.clients.urls')),
    path('cars/', include('apps.cars.urls')),
    path('warehouse/', include('apps.warehouse.urls')),
    path('worktypes/', include('apps.worktypes.urls')),
]

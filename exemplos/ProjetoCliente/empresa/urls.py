from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('core.urls_api')),
    path('customers', include('core.urls')),
    path('', include('core.urls')),
]

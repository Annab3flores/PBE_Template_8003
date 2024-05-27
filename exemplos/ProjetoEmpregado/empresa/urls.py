from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('empregados/', include('empregados.urls')),
    path('api/', include('empregados.urls_api')),
]

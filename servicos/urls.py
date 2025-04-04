from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('clinica.urls')),
    path('', include('agenda.ursl'))
]

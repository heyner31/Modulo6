from django.contrib import admin
from django.urls import path, include

# app_name = 'actividades'
urlpatterns = [
    path('', include('core.urls')),
    path('admin/', admin.site.urls),
    path('actividades/', include('actividades.urls')),
    path('blog/', include('blog.urls')),
]

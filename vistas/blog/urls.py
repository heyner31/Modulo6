from django.urls import path
from .views import BlogHome, BlogGenerador,BlogDetalle

app_name = 'blog'
urlpatterns = [
    path('', BlogHome.as_view(), name='home'),
    path('detalle/<int:pk>/', BlogDetalle.as_view(), name='detalle'),
    path('generador/', BlogGenerador.as_view(), name='generador'),
]

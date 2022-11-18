from django.urls import path
from .views import BlogHome, BlogGenerador,BlogDetalle, BlogCrear, BlogEditar,BlogEliminar

app_name = 'blog'
urlpatterns = [
    path('', BlogHome.as_view(), name='home'),
    path('detalle/<int:pk>/', BlogDetalle.as_view(), name='detalle'),
    path('generador/', BlogGenerador.as_view(), name='generador'),
    path('crear/', BlogCrear.as_view(), name="crear"),
    path('editar/<int:pk>/', BlogEditar.as_view(), name="editar"),
    path('eliminar/<int:pk>/', BlogEliminar.as_view(), name="eliminar"),
]

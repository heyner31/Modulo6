from django.urls import path
from . import views

app_name = 'actividades'
urlpatterns = [
    path('', views.ActividadesHome.as_view(), name='home'),
    path('generador/', views.ActividadesGenerador.as_view(), name='generador'),
    path('detalle/<int:pk>/', views.ActividadesDetalle.as_view(), name='detalle'),
    path('crear/', views.ActividadesCrear.as_view(), name="crear"),
    path('editar/<int:pk>/', views.ActividadesEditar.as_view(), name="editar"),
    path('eliminar/<int:pk>/', views.ActividadesEliminar.as_view(), name="eliminar"),
    # path('email/', views.ActividadesEmail.as_view(), name="email"),
]
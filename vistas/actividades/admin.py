from django.contrib import admin
from . import models

# Configuración del modelo Actividad para el panel de administrador
class EtiquetaImportanciaAdmin(admin.ModelAdmin):
    # Campos de solo lectura
    readonly_fields = ('fecha_creacion',)
    # Campos de búsqueda para la tabla
    # Para campos que son otras clases, eg. relaciones ForeignKey, se usa '__' para consultar el campo anidado
    # Ejemplo: 'campo_clase__id'
    search_fields = ('titulo',)

# Configuración del modelo Actividad para el panel de administrador
class EtiquetaEstadoAdmin(admin.ModelAdmin):
    # Campos de solo lectura
    readonly_fields = ('fecha_creacion',)
    # Campos de búsqueda para la tabla
    # Para campos que son otras clases, eg. relaciones ForeignKey, se usa '__' para consultar el campo anidado
    # Ejemplo: 'campo_clase__id'
    search_fields = ('titulo',)

# Configuración del modelo Actividad para el panel de administrador
class ActividadAdmin(admin.ModelAdmin):
    # Campos de solo lectura
    readonly_fields = ('fecha_creacion', 'fecha_actualizacion')
    # Columnas a mostrar en la tabla
    list_display = ('titulo', 'importancia', 'estado', 'fecha_inicio', 'fecha_limite', 'fecha_creacion', 'fecha_actualizacion')
    # Orden jerárquico de las columnas en la tabla. Usar '-' para invertir el orden.
    ordering = ('-fecha_actualizacion',)
    # Campos de búsqueda para la tabla
    # Para campos que son otras clases, eg. relaciones ForeignKey, se usa '__' para consultar el campo anidado
    # Ejemplo: 'campo_clase__id'
    search_fields = ('titulo',)
    # Campo para crear una jerarquía de fechas de filtro rápido (por mes y luego por día)
    date_hierarchy = 'fecha_inicio'
    # Campos de filtros
    list_filter = ('importancia', 'estado')


admin.site.register(models.EtiquetaImportancia, EtiquetaImportanciaAdmin)
admin.site.register(models.EtiquetaEstado, EtiquetaEstadoAdmin)
admin.site.register(models.Actividad, ActividadAdmin)

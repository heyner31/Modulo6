from django.db import models
from django.utils import timesince

class EtiquetaImportancia(models.Model):
    titulo =models.CharField(max_length=32, null=False, verbose_name="titulo")
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name="fecha creacion")

    def __str__(self):
        return self.titulo
    
    class Meta:
        verbose_name = "Etiqueta de importancia"
        verbose_name_plural = "Etiquetas de importancia"
        ordering = ['fecha_creacion']

class EtiquetaEstado(models.Model):
    titulo =models.CharField(max_length=32, null=False, verbose_name="titulo")
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name="fecha creacion")

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = "Etiqueta de estado"        
        verbose_name_plural = "Etiquetas de estado"
        ordering = ['fecha_creacion']

class Actividad(models.Model):
    titulo = models.CharField(max_length=256,null=False, verbose_name="Titulo")
    descripcion = models.TextField(verbose_name="descripcion", null=True, blank=True)
    fecha_inicio = models.DateField()
    fecha_limite = models.DateField(verbose_name="fecha limite")
    importancia = models.ForeignKey(EtiquetaImportancia, on_delete=models.CASCADE)
    estado = models.ForeignKey(EtiquetaEstado, on_delete=models.CASCADE)
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name="fecha creacion")
    fecha_actualizacion = models.DateTimeField(auto_now=True, verbose_name="fecha actualizacion")

    def __str__(self):
        return self.titulo

    @property
    def time_since(self):
        return timesince.timesince(self.fecha_creacion)

    class Meta:
        verbose_name = "Actividad"
        verbose_name_plural = "Actividades"
        ordering = ['-fecha_creacion']


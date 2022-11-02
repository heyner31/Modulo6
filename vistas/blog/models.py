from django.db import models

class EntradaBlog(models.Model):
    titulo =models.CharField(max_length=32, null=False, verbose_name="titulo")
    contenido = models.TextField(verbose_name='Contenido')

    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name="fecha creacion")
    fecha_actualizacion = models.DateTimeField(auto_now_add=True, verbose_name="fecha actualizacion")
    
    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = "Entrada de blog"
        verbose_name_plural = "Entradas de blog"
        ordering = ['fecha_creacion']



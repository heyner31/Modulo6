from django.contrib import admin
from .models import EntradaBlog

class EntradaBlogAdmin(admin.ModelAdmin):
    readonly_fields = ('fecha_creacion', 'fecha_actualizacion')
    list_display = ('titulo', 'fecha_creacion', 'fecha_actualizacion')
    
admin.site.register(EntradaBlog, EntradaBlogAdmin)
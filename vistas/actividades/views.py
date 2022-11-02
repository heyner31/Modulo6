from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views import View
from django.views.generic import TemplateView,RedirectView, ListView,DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse ,reverse_lazy
from .models import Actividad, EtiquetaEstado, EtiquetaImportancia

import pdb
import datetime
import random

# importes para uso del correo
from pathlib import Path
from django.core import mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from email.mime.image import MIMEImage
from django.conf import settings

# import lorem
# from lorem_text import lorem

# def home(request):
#     return HttpResponse("Pagina de inicio")

# class ActividadesHome(View):
#     def get(self, request):
#         pdb.set_trace()
#         return render(request, template_name = 'actividades/base.html')

#     def post(self, request):
#         return HttpResponse('Peticion POST')

# class ActividadesDetalle(TemplateView):
#     template_name = 'actividades/detalle.html'

# class ActividadesRedirec(RedirectView):
#     # url = 'https://www.google.com.mx/'
#     # pattern_name = 'actividades:detalle'

#     def get_redirect_url(self, *args, **kwargs):
#         return reverse('actividades:detalle')

class ActividadesHome(ListView):
    model = Actividad
    template_name = 'actividades/home.html'
    paginate_by = 3
    # nombre de la varieble del contexto, por defecto: '{modelo}_list'
    # context_object_name = 'elementos'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        param_get = '&'.join([f'{p}={k}' for p,k in self.request.GET.items() if p != 'page'])
        context["param_get"] = param_get
        return context

    def get_queryset(self):
        importancia_pk = self.request.GET.get('ipk', None)
        estado_pk = self.request.GET.get('epk', None)

        objetos = Actividad.objects.all()
        if importancia_pk:
            objetos = objetos.filter(importancia=importancia_pk)
        if estado_pk:
            objetos = objetos.filter(estado=estado_pk)

        
        return objetos

class ActividadesGenerador(View):
    def get(self, request):
        return render(request, template_name='actividades/generador.html')
    
    def post(self, request):
        # Número de actividades indicadas en el formulario
        cantidad = int(request.POST.get('cantidad', 0))
        # Fecha mínima de inicio de las actividades
        fecha_base = datetime.date(year=2022, month=1, day=1)
        # Lista de etiquetas existentes
        et_importancia = EtiquetaImportancia.objects.all()
        et_estado = EtiquetaEstado.objects.all()
        for _ in range(cantidad):
            actividad = Actividad()
            # actividad.titulo = lorem.sentence()
            # actividad.descripcion = lorem.paragraph()
            actividad.titulo = 'hola'
            actividad.descripcion = 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
            actividad.fecha_inicio = fecha_base + datetime.timedelta(days=random.randint(0, 100))
            actividad.fecha_limite = actividad.fecha_inicio + datetime.timedelta(days=random.randint(30, 90))
            actividad.importancia = et_importancia[random.randint(0, len(et_importancia) - 1)]
            actividad.estado = et_estado[random.randint(0, len(et_estado) - 1)]
            actividad.save()
            
        return redirect('actividades:home')


class ActividadesDetalle(DetailView):
    model = Actividad
    template_name = 'actividades/detalle.html'

class ActividadesCrear(CreateView):
    extra_context = {'importancias':EtiquetaImportancia.objects.all(),'estados':EtiquetaEstado.objects.all(), 'accion': 'crear'}
    template_name = 'actividades/crear.html'
    
    model = Actividad
    fields = ['titulo', 'descripcion', 'fecha_inicio', 'fecha_limite', 'importancia', 'estado']
    success_url = reverse_lazy('actividades:home')

    def post(self, request, *args, **kwargs):
        resp = super().post(request, *args, **kwargs)

        if self.object is not None:
            self.enviar_email(self.object, request)

        return resp
    
    def enviar_email(self, actividad, request):
        mail.send_mail(
            'Actividad nueva',
            f'Actividad nueva: \n{actividad.titulo}',
            settings.EMAIL_HOST_USER,
            [settings.EMAIL_HOST_USER],
            fail_silently=False,
        )

        # def enviar_email(self, actividad, request):
        # mail.send_mail(
        #     'Actividad nueva',
        #     f'Actividad nueva: \n{actividad.titulo}',
        #     settings.EMAIL_HOST_USER,
        #     [settings.EMAIL_HOST_USER],
        #     fail_silently=False,
        # )


class ActividadesEditar(UpdateView):
    model = Actividad
    template_name = 'actividades/crear.html'
    extra_context = {'importancias':EtiquetaImportancia.objects.all(),'estados':EtiquetaEstado.objects.all(), 'accion': 'editar'}
    fields = ['titulo', 'descripcion', 'fecha_inicio', 'fecha_limite', 'importancia', 'estado']

    def get_success_url(self):
        return reverse('actividades:detalle', args=(self.kwargs['pk'],))

class ActividadesEliminar(DeleteView):
    model = Actividad
    template_name = 'actividades/detalle.html'
    success_url = reverse_lazy('actividades:home')
    extra_context = {'confirmar_eliminar':True}


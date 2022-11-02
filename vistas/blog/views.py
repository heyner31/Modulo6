from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView
from .models import EntradaBlog
import pdb
import random

class BlogHome(ListView):
    model = EntradaBlog
    template_name = 'blog/home.html'
    paginate_by = 3

class BlogGenerador(View):
    def get(self, request):
        return render(request, template_name='blog/generador.html')
    
    def post(self, request):
        cantidad = int(request.POST.get('cantidad', 0))
        

        for _ in range(cantidad):
            numr = random.randint(0, 10000)
            entradablog = EntradaBlog()
            entradablog.titulo = 'Blog ' + str(numr)
            entradablog.contenido = 'Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old. Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia, looked up one of the more obscure Latin words, consectetur, from a Lorem Ipsum passage, and going through the cites of the word in classical literature, discovered the undoubtable source. Lorem Ipsum comes from sections 1.10.32 and 1.10.33 of "de Finibus Bonorum et Malorum" (The Extremes of Good and Evil) by Cicero, written in 45 BC. This book is a treatise on the theory of ethics, very popular during the Renaissance. The first line of Lorem Ipsum, "Lorem ipsum dolor sit amet..", comes from a line in section 1.10.32.'
            entradablog.save()
            
        return redirect('blog:home')

class BlogDetalle(DetailView):
    model = EntradaBlog
    template_name = 'blog/detalle.html'
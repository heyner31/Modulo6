from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views import View
from django.views.generic import TemplateView


class CoreHome(TemplateView):
    template_name = 'core/index.html'
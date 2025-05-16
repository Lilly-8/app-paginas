from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class VistaPaginaDeInicio(TemplateView):
    template_name = 'pagina de inicio.html'

class VistaPaginaAcercaDe(TemplateView):
    template_name = 'acerca de.html'
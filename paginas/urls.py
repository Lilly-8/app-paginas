from django.urls import path
from .views import VistaPaginaDeInicio, VistaPaginaAcercaDe

urlpatterns = [
    path('', VistaPaginaDeInicio.as_view(), name='pagina de inicio'),
    path('acerca de/', VistaPaginaAcercaDe.as_view(), name='acerca de'),
]

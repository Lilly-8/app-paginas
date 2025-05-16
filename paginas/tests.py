#from django.test import TestCase
from django.test import SimpleTestCase
from django.urls import reverse

# Create your tests here.
class PruebasPaginaDeInicio(SimpleTestCase):
    def test_la_url_existe_en_la_ubicacion_correcta(self):
        respuesta = self.client.get('/')
        self.assertEqual(respuesta.status_code, 200)

    def test_url_disponible_por_nombre(self):
        respuesta = self.client.get(reverse('pagina de inicio'))
        self.assertEqual(respuesta.status_code, 200)
    
    def test_nombre_correcto_de_la_plantilla(self):
        respuesta = self.client.get(reverse("pagina de inicio"))
        self.assertTemplateUsed(respuesta, "pagina de inicio.html")
    
    def test_contenido_de_la_plantilla(self):
        respuesta = self.client.get(reverse("pagina de inicio"))
        self.assertContains(respuesta, "<h1>Pagina de inicio</h1>")

class PruebasPaginaAcercaDe(SimpleTestCase):
    def test_la_url_existe_en_la_ubicacion_correcta(self):
        respuesta = self.client.get('/acerca de/')
        self.assertEqual(respuesta.status_code, 200)
    
    def test_url_disponible_por_nombre(self):
        respuesta = self.client.get(reverse('acerca de'))
        self.assertEqual(respuesta.status_code, 200)

    def test_nombre_correcto_de_la_plantilla(self):
        respuesta = self.client.get(reverse("acerca de"))
        self.assertTemplateUsed(respuesta, "acerca de.html")

    def test_contenido_de_la_plantilla(self):
        respuesta = self.client.get(reverse("acerca de"))
        self.assertContains(respuesta, "<h1>Pagina Acerca de</h1>")

class PruebaSencilla(SimpleTestCase):
    def test_codigo_de_estado_de_la_paginaDeInicio(self):
        respuesta = self.client.get('/')
        self.assertEqual(respuesta.status_code, 200)

    def test_codigo_de_estado_de_acercaDe(self):
        respuesta = self.client.get('/acerca de/')
        self.assertEqual(respuesta.status_code, 200)

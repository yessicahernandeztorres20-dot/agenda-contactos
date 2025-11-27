from django.test import TestCase
from .models import Categoria, Contacto

class ContactoModelTest(TestCase):
    def setUp(self):
        cat = Categoria.objects.create(nombre="Trabajo")
        Contacto.objects.create(nombre="Juan", telefono="12345678", categoria=cat)

    def test_contacto_nombre(self):
        contacto = Contacto.objects.get(nombre="Juan")
        self.assertEqual(contacto.nombre, "Juan")
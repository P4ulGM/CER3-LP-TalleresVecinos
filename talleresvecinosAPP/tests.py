from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from .models import Lugar, Categoria, Profesor, Taller
from .serializers import LugarSimpleSerializer
from rest_framework.test import APIClient


class SerializerTests(TestCase):
    def test_lugar_simple_serializer_model(self):
        lugar = Lugar.objects.create(nombre="Prueba", direccion="Dir")
        data = LugarSimpleSerializer(lugar).data
        self.assertEqual(data["nombre"], "Prueba")


class TallerViewSetTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.categoria = Categoria.objects.create(nombre="Aire Libre", descripcion="desc")
        self.profesor = Profesor.objects.create(nombre_completo="Prof Uno")
        self.lugar = Lugar.objects.create(nombre="Lugar", direccion="Dir")
        # Accepted and future
        Taller.objects.create(
            titulo="Futuro",
            fecha=timezone.now().date() + timezone.timedelta(days=1),
            duracion_horas=1,
            estado="aceptado",
            profesor=self.profesor,
            lugar=self.lugar,
            categoria=self.categoria,
        )
        # Pending
        Taller.objects.create(
            titulo="Pendiente",
            fecha=timezone.now().date() + timezone.timedelta(days=1),
            duracion_horas=1,
            estado="pendiente",
            profesor=self.profesor,
            lugar=self.lugar,
            categoria=self.categoria,
        )

    def test_anonymous_only_sees_accepted_future(self):
        url = reverse('talleres-list')
        response = self.client.get(url)
        self.assertEqual(len(response.json()), 1)

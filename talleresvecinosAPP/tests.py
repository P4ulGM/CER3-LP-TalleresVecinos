from django.test import TestCase
from .models import Lugar
from .serializers import LugarSimpleSerializer


class SerializerTests(TestCase):
    def test_lugar_simple_serializer_model(self):
        lugar = Lugar.objects.create(nombre="Prueba", direccion="Dir")
        data = LugarSimpleSerializer(lugar).data
        self.assertEqual(data["nombre"], "Prueba")

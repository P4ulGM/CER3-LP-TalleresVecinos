from .models import Taller, Profesor, Lugar, Categoria
from rest_framework import viewsets, permissions
from .serializers import (
    TallerSerializer,
    ProfesorSerializer,
    LugarSerializer,
    CategoriaSerializer,
)
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters import rest_framework as filters
from django.utils import timezone

import requests
from datetime import datetime

class ProfesorViewSet(viewsets.ModelViewSet):
    queryset = Profesor.objects.all()
    permission_classes = [permissions.IsAdminUser]
    serializer_class = ProfesorSerializer

class LugarViewSet(viewsets.ModelViewSet):
    queryset = Lugar.objects.all()
    permission_classes = [permissions.IsAdminUser]
    serializer_class = LugarSerializer

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    permission_classes = [permissions.IsAdminUser]
    serializer_class = CategoriaSerializer

class TallerFilter(filters.FilterSet):
    fecha__gte = filters.DateFilter(field_name='fecha', lookup_expr='gte')

    class Meta:
        model = Taller
        fields = ['categoria', 'estado', 'profesor', 'fecha__gte']


class TallerViewSet(viewsets.ModelViewSet):
    queryset = Taller.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = TallerSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = TallerFilter
    search_fields = ['titulo', 'observacion']
    ordering_fields = ['fecha', 'titulo']
    ordering = ['-fecha']

    def get_queryset(self):
        """Restrict queryset for anonymous users."""
        qs = super().get_queryset()
        user = self.request.user
        if not user.is_authenticated or not (user.is_staff or hasattr(user, 'juntadevecino')):
            qs = qs.filter(estado='aceptado', fecha__gte=timezone.now().date())
        return qs

    def obtener_info_feriado(self, fecha):
        """Devuelve si la fecha es feriado y si es irrenunciable."""
        try:
            response = requests.get('https://api.boostr.cl/holidays.json', timeout=5)
            if response.status_code == 200:
                data = response.json()
                if data.get('status') == 'success' and 'data' in data:
                    fecha_str = fecha.strftime('%Y-%m-%d')
                    for feriado in data['data']:
                        if feriado.get('date') == fecha_str:
                            return True, feriado.get('inalienable', False)
        except Exception as e:
            print(f"Error al consultar API de feriados: {e}")
        return False, False

    def perform_create(self, serializer):
        """Valida reglas de feriados al crear un taller."""
        fecha = serializer.validated_data.get('fecha')
        categoria_id = serializer.validated_data.get('categoria_id')

        if not self.request.user.is_staff:
            # Todos los talleres creados por usuarios no funcionarios quedan pendientes
            serializer.validated_data['estado'] = 'pendiente'

        es_feriado, irrenunciable = self.obtener_info_feriado(fecha)
        if irrenunciable:
            serializer.validated_data['estado'] = 'rechazado'
            serializer.validated_data['observacion'] = "No se programan talleres en feriados irrenunciables"
        elif es_feriado:
            categoria = Categoria.objects.filter(id=categoria_id).first()
            if not (categoria and categoria.nombre.lower() == 'aire libre'):
                serializer.validated_data['estado'] = 'rechazado'
                serializer.validated_data['observacion'] = "Sólo se programan talleres al aire libre en feriados"
            else:
                serializer.validated_data['estado'] = 'pendiente'

        serializer.save()

    def perform_update(self, serializer):
        """Valida reglas de feriados al actualizar un taller."""
        fecha = serializer.validated_data.get('fecha')
        categoria_id = serializer.validated_data.get('categoria_id')

        if not self.request.user.is_staff:
            serializer.validated_data['estado'] = 'pendiente'

        if fecha:
            es_feriado, irrenunciable = self.obtener_info_feriado(fecha)
            if irrenunciable:
                serializer.validated_data['estado'] = 'rechazado'
                serializer.validated_data['observacion'] = "No se programan talleres en feriados irrenunciables"
            elif es_feriado:
                categoria = Categoria.objects.filter(id=categoria_id).first()
                if not (categoria and categoria.nombre.lower() == 'aire libre'):
                    serializer.validated_data['estado'] = 'rechazado'
                    serializer.validated_data['observacion'] = "Sólo se programan talleres al aire libre en feriados"
                else:
                    serializer.validated_data['estado'] = 'pendiente'

        serializer.save()
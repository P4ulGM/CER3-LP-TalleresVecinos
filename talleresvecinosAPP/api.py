from .models import Taller, Profesor, Lugar, Categoria
from rest_framework import viewsets, permissions
from .serializers import TallerSerializer, ProfesorSerializer, LugarSerializer, CategoriaSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

class ProfesorViewSet(viewsets.ModelViewSet):
    queryset = Profesor.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ProfesorSerializer

class LugarViewSet(viewsets.ModelViewSet):
    queryset = Lugar.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = LugarSerializer

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = CategoriaSerializer

class TallerViewSet(viewsets.ModelViewSet):
    queryset = Taller.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = TallerSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['categoria', 'estado', 'profesor']
    search_fields = ['titulo', 'observacion']
    ordering_fields = ['fecha', 'titulo']
    ordering = ['-fecha']
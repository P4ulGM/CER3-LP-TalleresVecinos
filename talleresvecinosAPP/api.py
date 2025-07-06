from .models import Taller, Profesor, Lugar, Categoria
from rest_framework import viewsets, permissions
from .serializers import TallerSerializer, ProfesorSerializer, LugarSerializer, CategoriaSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

import requests
from datetime import datetime

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

    def es_feriado_irrenunciable(self, fecha):
        """
        Verifica si la fecha corresponde a un feriado irrenunciable
        consultando la API de feriados chilenos
        """
        try:
            # Hacer petición a la API de feriados
            response = requests.get('https://api.boostr.cl/holidays.json', timeout=5)
            
            if response.status_code == 200:
                response_data = response.json()
                
                # Verificar que la respuesta tenga la estructura esperada
                if response_data.get('status') == 'success' and 'data' in response_data:
                    feriados = response_data['data']
                    
                    # Convertir la fecha a string en formato YYYY-MM-DD
                    fecha_str = fecha.strftime('%Y-%m-%d')
                    
                    # Buscar si la fecha es un feriado irrenunciable
                    for feriado in feriados:
                        if (feriado.get('date') == fecha_str and 
                            feriado.get('inalienable') == True):
                            return True
                            
                return False
                
            else:
                return False
                
        except Exception as e:
            # En caso de error con la API, no rechazar el taller
            # pero se podría loggear el error
            print(f"Error al consultar API de feriados: {e}")
            return False

    def perform_create(self, serializer):
        """
        Sobrescribe el método de creación para validar feriados
        """
        fecha = serializer.validated_data.get('fecha')
        
        # Verificar si la fecha es un feriado irrenunciable
        if self.es_feriado_irrenunciable(fecha):
            # Modificar los datos antes de guardar
            serializer.validated_data['estado'] = 'rechazado'
            serializer.validated_data['observacion'] = "No se programan talleres en feriados irrenunciables"
        
        # Guardar el taller con los datos modificados
        serializer.save()

    def perform_update(self, serializer):
        """
        Sobrescribe el método de actualización para validar feriados
        """
        fecha = serializer.validated_data.get('fecha')
        
        # Solo verificar si se está actualizando la fecha
        if fecha and self.es_feriado_irrenunciable(fecha):
            # Modificar los datos antes de guardar
            serializer.validated_data['estado'] = 'rechazado'
            serializer.validated_data['observacion'] = "No se programan talleres en feriados irrenunciables"
        
        # Guardar el taller con los datos modificados
        serializer.save()
from .models import Taller, Profesor, Lugar
from rest_framework import viewsets, permissions
from .serializers import TallerSerializer, ProfesorSerializer, LugarSerializer

class ProfesorViewSet(viewsets.ModelViewSet):
    queryset = Profesor.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ProfesorSerializer

class LugarViewSet(viewsets.ModelViewSet):
    queryset = Lugar.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = LugarSerializer

class TallerViewSet(viewsets.ModelViewSet):
    queryset = Taller.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = TallerSerializer
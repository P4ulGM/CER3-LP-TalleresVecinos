from .models import Taller, Profesor
from rest_framework import viewsets, permissions
from .serializers import TallerSerializer, ProfesorSerializer

class ProfesorViewSet(viewsets.ModelViewSet):
    queryset = Profesor.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ProfesorSerializer

class TallerViewSet(viewsets.ModelViewSet):
    queryset = Taller.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = TallerSerializer
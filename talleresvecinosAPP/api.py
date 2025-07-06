from .models import Taller
from rest_framework import viewsets, permissions
from .serializers import TallerSerializer

class TallerViewSet(viewsets.ModelViewSet):
    queryset = Taller.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = TallerSerializer
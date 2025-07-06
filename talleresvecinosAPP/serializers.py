from rest_framework import serializers
from .models import Taller

class TallerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Taller
        fields = ('id', 'titulo', 'fecha', 'duracion_horas', 'estado', 'profesor', 'fecha_creacion', 
                  'fecha_modificacion', 'lugar', 'categoria', 'observacion')
        read_only_fields = ['fecha_creacion', 'fecha_modificacion',]

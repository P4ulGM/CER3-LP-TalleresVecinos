from rest_framework import serializers
from .models import Taller, Profesor

class ProfesorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profesor
        fields = ('id', 'nombre_completo')

class TallerSerializer(serializers.ModelSerializer):
    profesor = ProfesorSerializer(read_only=True)
    profesor_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Taller
        fields = ('id', 'titulo', 'fecha', 'duracion_horas', 'estado', 'profesor', 'profesor_id',
                  'lugar', 'categoria', 'observacion', 'fecha_creacion', 'fecha_modificacion')
        read_only_fields = ['fecha_creacion', 'fecha_modificacion']


from rest_framework import serializers
from .models import Taller, Profesor, Lugar, Categoria

class ProfesorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profesor
        fields = ('id', 'nombre_completo')

class LugarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lugar
        fields = ('id', 'nombre', 'direccion')

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ('id', 'nombre', 'descripcion')

class TallerSerializer(serializers.ModelSerializer):
    profesor = ProfesorSerializer(read_only=True)
    profesor_id = serializers.IntegerField(write_only=True)


    lugar = LugarSerializer(read_only=True)
    lugar_id = serializers.IntegerField(write_only=True)

    categoria = CategoriaSerializer(read_only=True)
    categoria_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Taller
        fields = ('id', 'titulo', 'fecha', 'duracion_horas', 'estado', 'profesor', 'profesor_id',
                  'lugar', 'lugar_id', 'categoria', 'categoria_id', 'observacion', 'fecha_creacion', 'fecha_modificacion')
        read_only_fields = ['fecha_creacion', 'fecha_modificacion']


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

class LugarSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lugar
        fields = ('id', 'nombre')

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ('id', 'nombre', 'descripcion')

class CategoriaSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ('id', 'nombre')  

class TallerSerializer(serializers.ModelSerializer):
    profesor = ProfesorSerializer(read_only=True)
    profesor_id = serializers.IntegerField(write_only=True)


    lugar = LugarSimpleSerializer(read_only=True)
    lugar_id = serializers.IntegerField(write_only=True)

    categoria = CategoriaSimpleSerializer(read_only=True)
    categoria_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Taller
        fields = ('id', 'titulo', 'fecha', 'duracion_horas', 'estado', 'profesor', 'profesor_id',
                  'lugar', 'lugar_id', 'categoria', 'categoria_id', 'observacion')
        read_only_fields = ['fecha_creacion', 'fecha_modificacion']


from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Juntadevecino(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name = "Junta de Vecino"
        verbose_name_plural = "Juntas de Vecinos"


class Taller(models.Model):
    ESTADO_CHOICES = [
        ('programado', 'Programado'),
        ('en_curso', 'En Curso'),
        ('finalizado', 'Finalizado'),
        ('cancelado', 'Cancelado'),
    ]
    
    CATEGORIA_CHOICES = [
        ('tecnologia', 'Tecnología'),
        ('salud', 'Salud'),
        ('educacion', 'Educación'),
        ('arte', 'Arte y Cultura'),
        ('deporte', 'Deporte'),
        ('cocina', 'Cocina'),
        ('manualidades', 'Manualidades'),
        ('otros', 'Otros'),
    ]
    
    titulo = models.CharField(max_length=200, verbose_name="Título")
    fecha = models.DateTimeField(verbose_name="Fecha y Hora")
    duracion_horas = models.DecimalField(max_digits=4, decimal_places=2, verbose_name="Duración (horas)")
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='programado', verbose_name="Estado")
    profesor = models.CharField(max_length=100, verbose_name="Profesor")
    lugar = models.CharField(max_length=200, verbose_name="Lugar")
    categoria = models.CharField(max_length=20, choices=CATEGORIA_CHOICES, verbose_name="Categoría")
    observacion = models.TextField(blank=True, null=True, verbose_name="Observaciones")
    
    # Campos adicionales útiles
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.titulo} - {self.fecha.strftime('%d/%m/%Y')}"
    
    class Meta:
        verbose_name = "Taller"
        verbose_name_plural = "Talleres"
        ordering = ['-fecha']
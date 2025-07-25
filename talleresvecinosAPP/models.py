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


class Profesor(models.Model):
    nombre_completo = models.CharField(max_length=150, verbose_name="Nombre Completo")
    
    def __str__(self):
        return self.nombre_completo
    
    class Meta:
        verbose_name = "Profesor"
        verbose_name_plural = "Profesores"
        ordering = ['nombre_completo']

class Lugar(models.Model):
    nombre = models.CharField(max_length=150, verbose_name="Nombre")
    direccion = models.CharField(max_length=255, verbose_name="Dirección")
    
    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = "Lugar"
        verbose_name_plural = "Lugares"

class Categoria(models.Model):
    nombre = models.CharField(max_length=150, verbose_name="Nombre")
    descripcion = models.CharField(max_length=255, verbose_name="Descripcion")
    
    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"


class Taller(models.Model):
    ESTADO_CHOICES = [
        ('pendiente', 'Pendiente'),
        ('aceptado', 'Aceptado'),
        ('rechazado', 'Rechazado'),
    ]
    
    
    titulo = models.CharField(max_length=200, verbose_name="Título")
    fecha = models.DateField(verbose_name="Fecha")
    duracion_horas = models.DecimalField(max_digits=4, decimal_places=2, verbose_name="Duración (horas)")
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='pendiente', verbose_name="Estado")
    profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE, verbose_name="Profesor")
    lugar = models.ForeignKey(Lugar, on_delete=models.CASCADE, verbose_name="Lugar")
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, verbose_name="Categoria")
    observacion = models.TextField(blank=True, null=True, verbose_name="Observaciones")
    
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.titulo} - {self.fecha}"
    
    class Meta:
        verbose_name = "Taller"
        verbose_name_plural = "Talleres"
        ordering = ['-fecha']
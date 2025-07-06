from django.contrib import admin
from .models import Juntadevecino, Taller, Profesor, Lugar, Categoria

# Register your models here.
admin.site.register(Juntadevecino)
admin.site.register(Taller)
admin.site.register(Profesor)
admin.site.register(Lugar)
admin.site.register(Categoria)

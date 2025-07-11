from django.urls import path, include
from .views import home, register, ver_talleres, taller_registrado

from rest_framework import routers
from .api import TallerViewSet, ProfesorViewSet, LugarViewSet, CategoriaViewSet

router = routers.DefaultRouter()

# Register the API routes
router.register('talleres', TallerViewSet, 'talleres')
router.register('profesores', ProfesorViewSet, 'profesores')
router.register('lugares', LugarViewSet, 'lugares')
router.register('categorias', CategoriaViewSet, 'categorias')

urlpatterns = [
    path('', home, name='home'),
    path('register/', register, name='register'),
    path('ver_talleres/', ver_talleres, name='ver_talleres'),
    path('taller_registrado/', taller_registrado, name='taller_registrado'),
    path('api/', include(router.urls)),
]
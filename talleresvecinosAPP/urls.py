from django.urls import path, include
from .views import home, register

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
    path('api/', include(router.urls)),
]
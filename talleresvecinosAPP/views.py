from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login
import requests
from django.utils import timezone
from .models import Categoria

# Create your views here.

def home(request):
    return render(request, 'app/home.html')

def register(request):
    data = {
        'form': CustomUserCreationForm()
    }

    if request.method == 'POST':
        user_creation_form = CustomUserCreationForm(data=request.POST)

        if user_creation_form.is_valid():
            user_creation_form.save()

            user = authenticate(username=user_creation_form.cleaned_data['username'], password=user_creation_form.cleaned_data['password1'])
            login(request, user)
            return redirect('home')
        else:
            data['form'] = user_creation_form

    return render(request, 'registration/register.html', data)

def ver_talleres(request):
    try:
        # Obtener el filtro de categoría desde la URL
        categoria_id = request.GET.get('categoria', '')
        
        # Construir la URL de la API con filtros
        api_url = f"{request.build_absolute_uri('/api/talleres/')}"
        params = {
            'estado': 'aceptado',
            'fecha__gte': timezone.now().date()
        }
        
        if categoria_id:
            params['categoria'] = categoria_id
        
        response = requests.get(api_url, params=params)
        
        if response.status_code == 200:
            talleres_data = response.json()
            if isinstance(talleres_data, list):
                talleres = talleres_data
            else:
                talleres = talleres_data.get('results', talleres_data)
        else:
            talleres = []

    except Exception as e:
        talleres = []
    
    # Obtener todas las categorías para el filtro
    categorias = Categoria.objects.all()
    
    context = {
        'talleres': talleres,
        'categorias': categorias,
        'categoria_seleccionada': categoria_id
    }
    return render(request, 'app/ver_talleres.html', context)

def taller_registrado(request):
    """
    Vista que redirecciona a la API de talleres
    """
    # Construir la URL completa de la API
    api_url = request.build_absolute_uri('/api/talleres/')
    
    # Redireccionar a la API
    return redirect(api_url)
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login
import requests
from django.conf import settings

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
        api_url = f"{request.build_absolute_uri('/api/talleres/')}"
        
        response = requests.get(api_url)
        
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
    
    context = {
        'talleres': talleres
    }
    return render(request, 'app/ver_talleres.html', context)
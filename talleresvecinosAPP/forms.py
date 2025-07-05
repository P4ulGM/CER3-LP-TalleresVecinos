from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    telefono = forms.CharField(max_length=20, required=True, label="Teléfono")
    direccion = forms.CharField(max_length=255, required=True, label="Dirección")

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'telefono', 'direccion', 'password1', 'password2']

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Este correo electrónico ya está registrado')
        return email
from django import forms
from . models import UsuarioBautismo
from . models import Pais
from django.contrib.auth.forms import AuthenticationForm


class PaisForm(forms.ModelForm):
    class Meta:
        model = Pais
        fields = [
            'nombre_Pais',
        ]

class LoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Usuario'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Contraseña'})
    )

class BautismoForm(forms.ModelForm):
    class Meta:
        model = UsuarioBautismo
        fields = [
            'libro',
            'folio',
            'fecha_nacimiento',
            'fecha_bautismo',
            'lugar_nacimiento',
            'nombreB',
            'apellidosB',
            'nombre_padre',
            'nombre_madre',
            'nombre_abuelo_paterno',
            'nombre_abuela_paterna',
            'nombre_abuelo_materno',
            'nombre_abuela_materna',
            'nombre_padrino',
            'nombre_madrina',
            'doy_fe',
            'tipo_hijo',
        ]
widgets = {
        'lugar': forms.TextInput(attrs={'placeholder': 'Escribe un lugar'}),
    }
        


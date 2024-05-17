from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from .models import Usuario


#Formulario de inicio de sesión
class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Usuario", max_length=30)
    password = forms.CharField(label="Contraseña", widget=forms.PasswordInput)

#Formulario de registro de usuario
class RegistrationForm(forms.ModelForm):
    password = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirmar contraseña", widget=forms.PasswordInput)
    rut = forms.CharField(label = "RUT", max_length=10)
    direccion = forms.CharField(label="Dirección", max_length=150)
    telefono = forms.CharField(label="Teléfono", max_length=12)
    correo_electronico = forms.EmailField(label="Correo electrónico")
    tipo_usuario = forms.ChoiceField(choices=Usuario.TIPO_USUARIO_CHOICES)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError("Las contraseñas no coinciden.")
        return cd['password2']
    
#Formulario edición de perfil
class EditProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
        
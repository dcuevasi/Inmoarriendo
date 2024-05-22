from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from .models import Usuario, Inmueble


#Formulario de inicio de sesión
class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Usuario", max_length=30)
    password = forms.CharField(label="Contraseña", widget=forms.PasswordInput)

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirmar contraseña", widget=forms.PasswordInput)
    nombre = forms.CharField(label="Nombre", max_length=100)
    apellidos = forms.CharField(label="Apellidos", max_length=100)
    rut = forms.CharField(label="RUT", max_length=10)
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

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
            usuario = Usuario(
                user=user,
                nombre=self.cleaned_data['nombre'],
                apellidos=self.cleaned_data['apellidos'],
                rut=self.cleaned_data['rut'],
                direccion=self.cleaned_data['direccion'],
                telefono=self.cleaned_data['telefono'],
                correo_electronico=self.cleaned_data['correo_electronico'],
                tipo_usuario=self.cleaned_data['tipo_usuario'],
            )
            usuario.save()
        return user
    
#Formulario edición de perfil
class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nombre', 'apellidos', 'direccion', 'telefono', 'correo_electronico', 'tipo_usuario']

#Formulario para ingresar datos de inmuebles
class InmuebleForm(forms.ModelForm):
    class Meta:
        model = Inmueble
        fields = [
            'nombre', 'descripcion', 'm2_construidos', 'm2_totales',
            'estacionamientos', 'habitaciones', 'baños', 'direccion',
            'comuna', 'tipo_inmueble', 'precio_mensual'
        ]
        
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .forms import LoginForm, RegistrationForm, EditProfileForm, InmuebleForm
from .models import Usuario, Inmueble, Comuna

# Create your views here.

def home_view(request):
    context = {}
    if request.user.is_authenticated:
        usuario = Usuario.objects.get(user=request.user)
        context = {
            'usuario': usuario,
            'tipo_usuario': usuario.tipo_usuario
        }
    return render(request, 'index.html', context)
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate (username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('profile')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form':form})

#Vista de registro
def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})

#Vista de perfil, requiere login        
@login_required
def profile_view(request):
    usuario = Usuario.objects.get(user=request.user)
    context = {
        'usuario': usuario,
        'tipo_usuario': usuario.tipo_usuario
    }
    return render(request, 'profile.html', context)
    

#Vista de perfil, requiere login   
@login_required
def edit_profile_view(request):
    usuario = Usuario.objects.get(user=request.user)

    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = EditProfileForm(instance=usuario)

    return render(request, 'edit_profile.html', {'form': form})

#Agregar inmueble, requiere login
@login_required
def agregar_inmueble_view(request):
    comunas = Comuna.objects.all()
    if request.method == 'POST':
        form = InmuebleForm(request.POST)
        if form.is_valid():
            inmueble = form.save(commit=False)
            inmueble.arrendador = request.user.usuario
            inmueble.save()
            return redirect('lista_inmuebles')
    else:
        form = InmuebleForm()
    return render(request, 'agregar_inmueble.html', {'form': form, 'comunas': comunas})

#Editar inmueble, requiere login
@login_required
def editar_inmueble_view(request, id):
    inmueble = Inmueble.objects.get(id=id, arrendador=request.user.usuario)
    if request.method == 'POST':
        form = InmuebleForm(request.POST, instance=inmueble)
        if form.is_valid():
            form.save()
            return redirect('lista_inmuebles')
    else:
        form = InmuebleForm(instance=inmueble)
    return render(request, 'editar_inmueble.html', {'form': form})

#Eliminar inmueble, requiere login
@login_required
def eliminar_inmueble_view(request, id):
    inmueble = Inmueble.objects.get(id=id, arrendador=request.user.usuario)
    if request.method == 'POST':
        inmueble.delete()
        return redirect('lista_inmuebles')
    return render(request, 'eliminar_inmueble.html', {'inmueble': inmueble})

#Listar inmuebles disponibles para arrendar
def listar_oferta_view(request):
    inmuebles = Inmueble.objects.all()
    return render(request, 'listar_oferta.html', {'inmuebles': inmuebles})

#Lista inmuebles propios, pero requiere login
@login_required
def lista_inmuebles_view(request):
    inmuebles = Inmueble.objects.filter(arrendador=request.user.usuario)
    return render(request, 'lista_inmuebles.html', {'inmuebles': inmuebles})

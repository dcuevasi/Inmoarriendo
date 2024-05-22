from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import home_view, login_view, register_view, profile_view, edit_profile_view, agregar_inmueble_view, listar_oferta_view, editar_inmueble_view, eliminar_inmueble_view, lista_inmuebles_view

urlpatterns = [
    path('', home_view, name='home'),
    path('login/', login_view, name = 'login'),
    path('register/', register_view, name ='register'),
    path('profile/', profile_view, name = 'profile'),
    path('edit_profile/', edit_profile_view, name = 'edit_profile'),
    path('logout/', LogoutView.as_view(next_page='/login/'), name='logout'),
    path('agregar_inmueble/', agregar_inmueble_view, name='agregar_inmueble'),
    path('lista_inmuebles/', lista_inmuebles_view, name='lista_inmuebles'),
    path('editar_inmueble/<int:id>/', editar_inmueble_view, name='editar_inmueble'),
    path('eliminar_inmueble/<int:id>/', eliminar_inmueble_view, name='eliminar_inmueble'),
    path('oferta/', listar_oferta_view, name='listar_oferta'),

]
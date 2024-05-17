from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import login_view, register_view, profile_view, edit_profile_view

urlpatterns = [
    path('login/', login_view, name = 'login'),
    path('register/', register_view, name ='register'),
    path('profile/', profile_view, name = 'profile'),
    path('edit_profile/', edit_profile_view, name = 'edit_profile'),
    path('logout/', LogoutView.as_view(next_page='/login/'), name='logout'),

]
from django import forms
from django.contrib.auth.forms import UserCreationForm #Este es un form que incorpora django para registrar un usuario nuevo!!!
from django.contrib.auth.models import User #importo el modelo de usuario que viene incorporado en django
# from user.models import User #EN VEZ DE UTILIZAR EL MODELO DE USUARIO QUE INCORPORA DJANGO POR DEFECTO, TRAIGO EL QUE EXTENDÍ YO EN LA APP USER

# Creo una clase que va a utilizar el formulario por defecto de Django para crear un nuevo usuario, pero lo extiendo, ya que 
# el form de registracion por defecto de django solo pide usuario y contraseña,
# yo al extenderlo hago que pida también el nombre, apellido y email
class CustomUserCreationForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
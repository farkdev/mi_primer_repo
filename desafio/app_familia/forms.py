from unittest.util import _MAX_LENGTH
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class nuevo_formulario(forms.Form):
    nombre= forms.CharField(max_length=30)
    edad = forms.IntegerField()
    nacimiento = forms.DateField()
    vinculo = forms.CharField(max_length=15)
    apellido = forms.CharField(max_length=20)
    calle = forms.CharField(max_length=20)

class UserEditForm(UserCreationForm):
    email = forms.EmailField(label="Modificar email")
    password1: forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2: forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2']
        help_text = {k:"" for k in fields}
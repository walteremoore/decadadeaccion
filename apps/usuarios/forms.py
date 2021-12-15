from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from .models import Usuario
from datetime import datetime

class DateInput(forms.DateInput):
    input_type='date'

class UsuarioForm(UserCreationForm):
	username=forms.CharField(label="Nombre de usuario", widget=forms.TextInput(attrs={"class": "form-control", "placeholder":"Ingrese nombre de usuario"}))
	first_name=forms.CharField(label="Nombre/s", widget=forms.TextInput(attrs={"class": "form-control", "placeholder":"Ingrese nombre/s"}))
	last_name=forms.CharField(label="Apellido/s", widget=forms.TextInput(attrs={"class": "form-control", "placeholder":"Ingrese su apellido/s"}))
	dni=forms.CharField(label="Nro DNI", widget=forms.TextInput(attrs={"class": "form-control", "placeholder":"Ingrese su número de DNI sin puntos"}))
	email=forms.CharField(label="Correo Electronico", widget=forms.TextInput(attrs={"class": "form-control", "placeholder":"Ingrese su EMAIL"}))
	telefono=forms.CharField(label="Tel/Cel", widget=forms.TextInput(attrs={"class": "form-control", "placeholder":"Ingrese su número de telefono"}))
	direccion=forms.CharField(label="Dirección", widget=forms.TextInput(attrs={"class": "form-control", "placeholder":"Ingrese su Dirección"}))
	ciudad=forms.CharField(label="Ciudad", widget=forms.TextInput(attrs={"class": "form-control", "placeholder":"Ingrese su Ciudad"}))
	provincia=forms.CharField(label="Provincia", widget=forms.TextInput(attrs={"class": "form-control", "placeholder":"Ingrese su Provincia"}))
	pais=forms.CharField(label="País", widget=forms.TextInput(attrs={"class": "form-control", "placeholder":"Ingrese su País"}))
	foto=forms.CharField(label="Fotografía URL", widget=forms.TextInput(attrs={"class": "form-control", "placeholder":"Ingrese la URL de su Fotografía"}))
	
	class Meta:
		model = Usuario
		fields = ["username", "first_name", "last_name", "email", "dni", "telefono", "direccion", "ciudad", "provincia", "pais", "foto", "fecha_nacimiento"]
		widgets = {
            'fecha_nacimiento': DateInput(),
        	}
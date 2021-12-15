from django import forms
from django.forms import ModelForm
from .models import Articulo
from datetime import datetime

class DateInput(forms.DateInput):
    input_type='date'

class ArticuloForm(forms.ModelForm):
    titulo = forms.CharField(label="Título del artículo", widget=forms.TextInput(attrs={"class":"form-control", "placeholder":"Por favor ingrese el título del artículo"}))
    imagen=forms.CharField(label="Fotografía URL", widget=forms.TextInput(attrs={"class": "form-control", "placeholder":"Ingrese la URL de su Fotografía"}))
    contenido=forms.CharField(widget=forms.Textarea(attrs={"class":"form-control"}))

    class Meta:
        model = Articulo
        fields = ["titulo", "contenido", "visibilidad", "categoria", "etiquetas", "imagen", "fecha_publicacion"]
        widgets = {
            'fecha_publicacion': DateInput(),
        }
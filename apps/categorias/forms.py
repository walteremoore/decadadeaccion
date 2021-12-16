from django import forms
from django.forms import ModelForm
from .models import Categoria

class CategoriaForm(forms.ModelForm):
    nombre = forms.CharField(label="Nombre de la Categoria", widget=forms.TextInput(attrs={"class":"form-control", "placeholder":"Por favor ingrese el nombre de la categoria"}))
    descripcion=forms.CharField(widget=forms.Textarea(attrs={"class":"form-control"}))

    class Meta:
        model = Categoria
        fields = ["nombre", "descripcion"]
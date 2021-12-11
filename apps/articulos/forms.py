from django import forms
from .models import Articulo

class ArticuloForm(forms.ModelForm):
    titulo = forms.CharField(label="Título del artículo", widget=forms.TextInput(attrs={"class":"form-control", "placeholder":"Por favor ingrese el título del artículo"}))
    class Meta:
        model = Articulo
        fields = ["titulo", "contenido"]
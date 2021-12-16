from django import forms
from django.forms import ModelForm
from apps.comentarios.models import Comentario

class ComentarioForm(forms.ModelForm):
    titulo = forms.CharField(label="Título del comentario", widget=forms.TextInput(attrs={"class":"form-control", "placeholder":"Por favor ingrese el título del comentario"}))
    contenido=forms.CharField(widget=forms.Textarea(attrs={"class":"form-control"}))

    class Meta:
        model = Comentario
        fields = ["titulo", "contenido"]

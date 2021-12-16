from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView 
from .forms  import UsuarioForm
from .models import Usuario

class Registrarme(CreateView):
	template_name = "usuarios/registrar.html"
	model = Usuario
	form_class = UsuarioForm

	def get_success_url(self, **kwargs):
		return reverse_lazy("login")
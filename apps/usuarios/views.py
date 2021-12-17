from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView 
from .forms  import UsuarioForm
from .models import Usuario
from apps.articulos.models import Articulo
from apps.categorias.models import Categoria
from apps.comentarios.models import Comentario
from django.views.generic import ListView, CreateView
from django.views.generic.edit import UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from apps.core.mixins import AdminRequiredMixins
from .forms  import UsuarioForm
from django.db.models import Q

class Registrarme(CreateView):
	template_name = "usuarios/registrar.html"
	model = Usuario
	form_class = UsuarioForm

	def get_success_url(self, **kwargs):
		return reverse_lazy("login")

class ListarAdmin(LoginRequiredMixin, AdminRequiredMixins, ListView):
    template_name="usuarios/admin/listar.html"
    model = Usuario
    context_object_name="usuarios"
    paginate_by = 20

    def get_context_data(self, **kwargs):
        context = super(ListarAdmin, self).get_context_data(**kwargs)
        context["busqueda_titulo"] = self.request.GET.get("titulo_usuario", "")
        return context

    def get_queryset(self):
        busqueda_titulo = self.request.GET.get("titulo_usuario", "")
        query = Usuario.objects.all().order_by("id")
        if len(busqueda_titulo) > 0:
            query = query.filter(Q(dni__icontains=busqueda_titulo)|
                                 Q(email__icontains=busqueda_titulo)).distinct()
            return query
        else:
            return Usuario.objects.all().order_by("id")

class MisUsuarios(LoginRequiredMixin, AdminRequiredMixins, ListView):
	template_name="usuarios/admin/listar.html"
	model = Usuario
	context_object_name="usuarios"
	
	def get_queryset(self):
		return Usuario.objects.filter(autor__id=self.request.user.id)	


class NuevoAdmin(LoginRequiredMixin, CreateView):
    template_name = "usuarios/admin/nuevo.html"
    model = Usuario
    form_class = UsuarioForm

    def get_success_url(self, **kwargs):
        return reverse_lazy("usuarios:admin_listar")

    def form_valid(self, form):
        f = form.save(commit=False)
        f.usuario_id = self.request.user.id
        return super(NuevoAdmin, self).form_valid(form)


class EditarAdmin(UpdateView):
    template_name = "usuarios/admin/editar.html"
    model = Usuario
    form_class = UsuarioForm
    context_object_name="usuario"

    def get_success_url(self, **kwargs):
        return reverse_lazy("usuarios:admin_listar")

class EliminarAdmin(LoginRequiredMixin, DeleteView):
    model = Usuario
    
    def get_success_url(self, **kwargs):
        return reverse_lazy("usuarios:mis_usuarios")

class Detalle (DetailView):
    template_name = "usuarios/detalle.html"
    model = Articulo
    context_object_name="usuarios"
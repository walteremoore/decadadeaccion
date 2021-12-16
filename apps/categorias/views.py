from django.shortcuts import render
from apps.articulos.models import Articulo
from apps.categorias.models import Categoria
from apps.comentarios.models import Comentario
from django.views.generic import ListView, CreateView
from django.views.generic.edit import UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from apps.core.mixins import AdminRequiredMixins
from .forms  import CategoriaForm
from django.db.models import Q

class ListarAdmin(LoginRequiredMixin, AdminRequiredMixins, ListView):
    template_name="categorias/admin/listar.html"
    model = Categoria
    context_object_name="categorias"
    paginate_by = 20

    def get_context_data(self, **kwargs):
        context = super(ListarAdmin, self).get_context_data(**kwargs)
        context["busqueda_titulo"] = self.request.GET.get("nombre_categoria", "")
        return context

    def get_queryset(self):
        busqueda_titulo = self.request.GET.get("nombre_categoria", "")
        query = Categoria.objects.all().order_by("nombre")
        if len(busqueda_titulo) > 0:
            query = query.filter(Q(nombre__icontains=busqueda_titulo)|
                                 Q(descripcion__icontains=busqueda_titulo)).distinct()
            return query
        else:
            return Categoria.objects.all().order_by("nombre")

class MisCategorias(LoginRequiredMixin, AdminRequiredMixins, ListView):
	template_name="categorias/admin/listar.html"
	model = Categoria
	context_object_name="categorias"
	
	def get_queryset(self):
		return Categoria.objects.filter(autor__id=self.request.user.id)	


class NuevoAdmin(LoginRequiredMixin, CreateView):
    template_name = "categorias/admin/nuevo.html"
    model = Categoria
    form_class = CategoriaForm

    def get_success_url(self, **kwargs):
        return reverse_lazy("categorias:admin_listar")

    def form_valid(self, form):
        f = form.save(commit=False)
        f.usuario_id = self.request.user.id
        return super(NuevoAdmin, self).form_valid(form)


class EditarAdmin(UpdateView):
    template_name = "categorias/admin/editar.html"
    model = Categoria
    form_class = CategoriaForm
    context_object_name="categoria"

    def get_success_url(self, **kwargs):
        return reverse_lazy("categorias:admin_listar")

class EliminarAdmin(LoginRequiredMixin, DeleteView):
    model = Categoria
    
    def get_success_url(self, **kwargs):
        return reverse_lazy("categorias:admin_listar")

class Detalle (DetailView):
    template_name = "categorias/detalle.html"
    model = Categoria
    context_object_name="categoria"
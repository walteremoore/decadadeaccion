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
from .forms  import ComentarioForm
from django.db.models import Q

class ListarAdmin(LoginRequiredMixin, AdminRequiredMixins, ListView):
    template_name="comentarios/admin/listar.html"
    model = Comentario
    context_object_name="comentarios"
    paginate_by = 20

    def get_context_data(self, **kwargs):
        context = super(ListarAdmin, self).get_context_data(**kwargs)
        context["busqueda_titulo"] = self.request.GET.get("titulo_comentario", "")
        return context

    def get_queryset(self):
        busqueda_titulo = self.request.GET.get("titulo_comentario", "")
        query = Comentario.objects.all().order_by("titulo")
        if len(busqueda_titulo) > 0:
            query = query.filter(Q(titulo__icontains=busqueda_titulo)|
                                 Q(contenido__icontains=busqueda_titulo)).distinct()
            return query
        else:
            return Comentario.objects.all().order_by("titulo")

class MisComentarios(LoginRequiredMixin, AdminRequiredMixins, ListView):
	template_name="comentarios/admin/listar.html"
	model = Comentario
	context_object_name="comentarios"
	
	def get_queryset(self):
		return Comentario.objects.filter(autor__id=self.request.user.id)	


class NuevoAdmin(LoginRequiredMixin, CreateView):
    template_name = "comentarios/admin/nuevo.html"
    model = Comentario
    form_class = ComentarioForm

    def get_success_url(self, **kwargs):
        return reverse_lazy("comentarios:admin_listar")

    def form_valid(self, form):
        f = form.save(commit=False)
        f.usuario_id = self.request.user.id
        return super(NuevoAdmin, self).form_valid(form)


class EditarAdmin(UpdateView):
    template_name = "comentarios/admin/editar.html"
    model = Comentario
    form_class = ComentarioForm
    context_object_name="comentario"

    def get_success_url(self, **kwargs):
        return reverse_lazy("comentarios:admin_listar")

class EliminarAdmin(LoginRequiredMixin, DeleteView):
    model = Comentario
    
    def get_success_url(self, **kwargs):
        return reverse_lazy("comentarios:admin_listar")

class Detalle (DetailView):
    template_name = "comentarios/detalle.html"
    model = Comentario
    context_object_name="comentario"
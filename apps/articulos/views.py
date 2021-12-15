from django.shortcuts import render
from apps.articulos.models import Articulo
from apps.categorias.models import Categoria
from apps.comentarios.models import Comentario
from django.views.generic import ListView, CreateView
from django.views.generic.edit import UpdateView, DeleteView
from .forms import ArticuloForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from apps.core.mixins import AdminRequiredMixins
from .forms  import ArticuloForm

def detalle(request):
    contex = {}
    return render(request, "articulos/detalle.html", contex)

class ListarAdmin(LoginRequiredMixin, AdminRequiredMixins, ListView):
    template_name="articulos/admin/listar.html"
    model = Articulo
    context_object_name="articulos"
    paginate_by = 20

def get_context_data(self, **kwargs):
	context = super(ListarAdmin, self).get_context_data(**kwargs)
	context["titulo_buscado"] = self.request.GET.get("titulo_articulo", "")
	return context

def get_queryset(self):
    busqueda_titulo = self.request.GET.get("titulo_articulo", "")
    query = Articulo.objects.all().order_by("titulo")
    if len(busqueda_titulo) > 0:
	    query = query.filter(nombre__icontains=busqueda_titulo)
    return query

class MisArticulos(LoginRequiredMixin, AdminRequiredMixins, ListView):
	template_name="articulos/admin/listar.html"
	model = Articulo
	context_object_name="articulos"
	
	def get_queryset(self):
		# self.request
		return Articulo.objects.filter(autor__id=self.request.user.id)	


class NuevoAdmin(LoginRequiredMixin, AdminRequiredMixins, CreateView):
    template_name = "articulos/admin/nuevo.html"
    model = Articulo
    form_class = ArticuloForm

    def get_success_url(self, **kwargs):
        return reverse_lazy("articulos:admin_listar")

    def form_valid(self, form):
        f = form.save(commit=False)
        f.usuario_id = self.request.user.id
        return super(NuevoAdmin, self).form_valid(form)


class EditarAdmin(LoginRequiredMixin, AdminRequiredMixins, UpdateView):
    template_name = "articulos/admin/editar.html"
    model = Articulo
    form_class = ArticuloForm

    def get_success_url(self, **kwargs):
        return reverse_lazy("articulos:admin_listar")

class EliminarAdmin(LoginRequiredMixin, AdminRequiredMixins, DeleteView):
    model = Articulo
    
    def get_success_url(self, **kwargs):
        return reverse_lazy("articulos:admin_listar")
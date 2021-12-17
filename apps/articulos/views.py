from django.shortcuts import render, redirect
from apps.articulos.models import Articulo
from apps.categorias.models import Categoria
from apps.comentarios.models import Comentario
from django.views.generic import ListView, CreateView
from django.views.generic.edit import UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from apps.core.mixins import AdminRequiredMixins
from .forms  import ArticuloForm
from django.db.models import Q

class ListarAdmin(LoginRequiredMixin, AdminRequiredMixins, ListView):
    template_name="articulos/admin/listar.html"
    model = Articulo
    context_object_name="articulos"
    paginate_by = 20

    def get_context_data(self, **kwargs):
        context = super(ListarAdmin, self).get_context_data(**kwargs)
        context["busqueda_titulo"] = self.request.GET.get("titulo_articulo", "")
        return context

    def get_queryset(self):
        busqueda_titulo = self.request.GET.get("titulo_articulo", "")
        query = Articulo.objects.all().order_by("titulo")
        if len(busqueda_titulo) > 0:
            query = query.filter(Q(titulo__icontains=busqueda_titulo)|
                                 Q(contenido__icontains=busqueda_titulo)).distinct()
            return query
        else:
            return Articulo.objects.all().order_by("titulo")

class MisArticulos(LoginRequiredMixin, ListView):
	template_name="articulos/admin/listar.html"
	model = Articulo
	context_object_name="articulos"
	
	def get_queryset(self):
		return Articulo.objects.filter(autor__id=self.request.user.id)	


class NuevoAdmin(LoginRequiredMixin, CreateView):
    template_name = "articulos/admin/nuevo.html"
    model = Articulo
    form_class = ArticuloForm

    def get_success_url(self, **kwargs):
        return reverse_lazy("articulos:mis_articulos")

    def form_valid(self, form):
        f = form.save(commit=False)
        f.autor_id = self.request.user.id
        return super(NuevoAdmin, self).form_valid(form)


class EditarAdmin(UpdateView):
    template_name = "articulos/admin/editar.html"
    model = Articulo
    form_class = ArticuloForm
    context_object_name="articulo"

    def get_success_url(self, **kwargs):
        return reverse_lazy("articulos:mis_articulos")

class BorrarLogicoAdmin(UpdateView):
    template_name = "articulos/admin/eliminar.html"
    model = Articulo
    #form_class = ArticuloBorrarLogicoForm
    context_object_name="articulo"

    def get_success_url(self, **kwargs):
        return reverse_lazy("articulos:mis_articulos")
    
class EliminarAdmin(LoginRequiredMixin, DeleteView):
    model = Articulo
    
    def get_success_url(self, **kwargs):
        return reverse_lazy("articulos:mis_articulos")

class Detalle (DetailView):
    template_name = "articulos/detalle.html"
    model = Articulo
    context_object_name="articulo"

def bajaLogica(request, aid):
    try:
        p = Articulo.objects.get(pk=aid)
        p.estado = 2
        p.save()
        return redirect("/")
    except Poll.DoesNotExist:
        raise Http404("Poll does not exist")
    return render(request, 'articulos/admin/eliminar.html', {'articulo': p})



def restaurarArticulo(request, aid):
    try:
        p = Articulo.objects.get(pk=aid)
        p.estado = 1
        p.save()
        return redirect("/")
    except Poll.DoesNotExist:
        raise Http404("Poll does not exist")
    return render(request, 'articulos/admin/eliminar.html', {'articulo': p})
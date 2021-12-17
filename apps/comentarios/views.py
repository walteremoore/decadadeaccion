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
from .forms  import ComentarioForm
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect

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

class MisComentarios(LoginRequiredMixin, ListView):
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
        return reverse_lazy("comentarios:mis_comentarios")

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
        return reverse_lazy("comentarios:mis_comentarios")

class EliminarAdmin(LoginRequiredMixin, DeleteView):
    model = Comentario
    
    def get_success_url(self, **kwargs):
        return reverse_lazy("comentarios:mis_comentarios")

class Detalle (DetailView):
    template_name = "comentarios/detalle.html"
    model = Comentario
    context_object_name="comentario"

def bajaLogicaCom(request, aid):
    try:
        p = Comentario.objects.get(pk=aid)
        p.estado = False
        p.save()
        return redirect("/")
    except Poll.DoesNotExist:
        raise Http404("Poll does not exist")
    return render(request, 'articulos/admin/eliminar.html', {'articulo': p})

def restaurarCom(request, aid):
    try:
        p = Comentario.objects.get(pk=aid)
        p.estado = True
        p.save()
        return redirect("/")
    except Poll.DoesNotExist:
        raise Http404("Poll does not exist")
    return render(request, 'articulos/admin/eliminar.html', {'articulo': p})

def comentarioNuevo(request, aid):
    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            articulo = Articulo.objects.get(pk=aid)
            comentario.articulo = articulo
            comentario.autor = request.user
            comentario.save()
            return HttpResponseRedirect('/')   
    else:   
        form = ComentarioForm()
    return render(request, 'comentarios/admin/nuevo.html', {'form': form})

def aprobarCom(request, cid):
    p = Comentario.objects.get(pk=cid)
    p.visibilidad = True
    p.save()
    return redirect("/")
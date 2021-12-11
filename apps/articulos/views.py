from django.shortcuts import render
from apps.articulos.models import Articulo
from django.views.generic import ListView, CreateView
from .forms import ArticuloForm
from django.urls import reverse_lazy

def detalle(request):
    contex = {}
    return render(request, "articulo/detalle.html", contex)

class ListarAdmin(ListView):
    template_name="articulos/admin/listar.html"
    model = Articulo
    context_object_name="articulos"

    # def get_queryset(self):
    #     self.request
    #     return Articulo.objects.filter(id=1)
    
class NuevoAdmin(CreateView):
    template_name = "articulos/admin/nuevo.html"
    model = Articulo
    form_class = ArticuloForm

    def get_success_url(self, **kwargs):
        return reverse_lazy("articulos:admin_listar")
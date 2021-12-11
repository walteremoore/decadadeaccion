from django.shortcuts import render
from apps.articulos.models import Articulo
from django.views.generic import ListView

def detalle(request):
    contex = {}
    return render(request, "articulo/detalle.html", contex)

class ListarAdmin(ListView):
    template_name="articulos/admin/listar.html"
    model = Articulo
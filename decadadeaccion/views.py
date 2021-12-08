from django.shortcuts import render
from apps.articulos.models import Articulo

def inicio(request):
    contex = {
        "articulos": Articulo.objects.all()
    }
    return render(request, "inicio.html", contex)

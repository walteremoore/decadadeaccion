#from django.shortcuts import render
from apps.articulos.models import Articulo
from django.views.generic.base import TemplateView

""" def inicio(request):
    contex = {
        "articulos": Articulo.objects.all()
    }
    return render(request, "inicio.html", contex)
 """

class Inicio(TemplateView):
    template_name = "inicio.html"

    def get_context_data(self, **kwargs):
        context = super(Inicio, self).get_context_data(**kwargs)
        context["articulos"] = Articulo.objects.all()
        return context
    
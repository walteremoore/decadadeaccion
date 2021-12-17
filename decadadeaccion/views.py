from django.shortcuts import render
from apps.articulos.models import Articulo
from django.views.generic.base import TemplateView
from django.contrib.auth.decorators import login_required
from apps.core.decorators  import admin_required
from django.views.generic import ListView
from django.db.models import Q

""" def inicio(request): # Basado en funciones
    contex = {
        "articulos": Articulo.objects.all()
    }
    return render(request, "inicio.html", contex)
 """

""" class Inicio(TemplateView): # Basado en clases
    template_name = "inicio.html"

    def get_context_data(self, **kwargs):
        context = super(Inicio, self).get_context_data(**kwargs)
        context["articulos"] = Articulo.objects.all()
        return context """

class Inicio(ListView):
    template_name="inicio.html"
    model = Articulo
    context_object_name="articulos"

    def get_context_data(self, **kwargs):
        context = super(Inicio, self).get_context_data(**kwargs)
        context["busqueda_articulo"] = self.request.GET.get("titulo_articulo", "")
        return context

    def get_queryset(self):
        busqueda_titulo = self.request.GET.get("titulo_articulo", "")
        query = Articulo.objects.all().order_by("titulo")
        if len(busqueda_titulo) > 0:
            query = query.filter(Q(titulo__icontains=busqueda_titulo)|
                                 Q(contenido__icontains=busqueda_titulo)).distinct()
            return query
        else:
            return Articulo.objects.filter(visibilidad=1,estado=1)
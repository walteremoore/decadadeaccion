from django.shortcuts import render
from apps.articulos.models import Articulo
from django.views.generic.base import TemplateView
from django.contrib.auth.decorators import login_required
from apps.core.decorators  import admin_required
from django.views.generic import ListView

# Basado en funciones
""" def inicio(request):
    contex = {
        "articulos": Articulo.objects.all()
    }
    return render(request, "inicio.html", contex)
 """
# Basado en clases
""" class Inicio(TemplateView):
    template_name = "inicio.html"

    def get_context_data(self, **kwargs):
        context = super(Inicio, self).get_context_data(**kwargs)
        context["articulos"] = Articulo.objects.all()
        return context """
    
class Inicio(ListView):
	template_name="inicio.html"
	model = Articulo
	context_object_name="articulos"
	
	def get_queryset(self):
		# self.request
		return Articulo.objects.filter(visibilidad=1)	
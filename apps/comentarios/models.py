from django.db import models
from apps.articulos.models import Articulo
from apps.usuarios.models import Usuario

class Comentario(models.Model):
    articulo = models.ForeignKey(Articulo, on_delete=models.CASCADE)
    contenido = models.TextField(blank=True, null=True)
    estado = models.BooleanField(blank=True, null=True, default=True) # True=aprobado, False=baja_logica
    visibilidad = models.BooleanField(blank=True, null=True, default=False) # True=visible, False=pendiente de moderar
    autor = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    titulo = models.CharField(max_length=255)
    
    class Meta:
	    db_table="comentarios"

    def __str__(self):
        return self.contenido

    def aprobar(self):
        self.visibilidad = True
        self.estado = True

    def rechazar(self):
        self.visibilidad = False
        self.estado = False
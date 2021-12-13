from django.db import models

class Comentario(models.Model):
    articulo = models.CharField(max_length=255, blank=True, null=True)
    contenido = models.TextField(blank=True, null=True)
    estado = models.BooleanField(blank=True, null=True)
    autor = models.CharField(max_length=255, blank=True, null=True)
    fecha_creacion = models.DateField(blank=True, null=True)
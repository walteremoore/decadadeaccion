from django.db import models

class Articulo(models.Model):
    titulo = models.CharField(max_length=255, blank=True, null=True)
    contenido = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.titulo #devuelvo el titulo del articulo
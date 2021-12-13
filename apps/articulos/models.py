from django.db import models

class Articulo(models.Model):
    titulo = models.CharField(max_length=255, blank=True, null=True)
    contenido = models.TextField(blank=True, null=True)
    estado = models.BooleanField(blank=True, null=True)
    visibilidad = models.BooleanField(blank=True, null=True)
    autor = models.CharField(max_length=255, blank=True, null=True)
    categoria = models.CharField(max_length=255, blank=True, null=True)
    etiquetas = models.CharField(max_length=255, blank=True, null=True)
    imagen = models.ImageField(null = True, blank=True, upload_to="images/")
    fecha_creacion = models.DateField(blank=True, null=True)
    fecha_publicacion = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.titulo #devuelvo el titulo del articulo

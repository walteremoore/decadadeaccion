from django.db import models
from apps.usuarios.models import Usuario
from apps.categorias.models import Categoria

class Articulo(models.Model):
    titulo = models.CharField(max_length=255, blank=True, null=True)
    contenido = models.TextField(blank=True, null=True)
    estado = models.BooleanField(blank=True, null=True)
    visibilidad = models.BooleanField(blank=True, null=True)
    autor = models.ForeignKey(Usuario, on_delete=models.CASCADE, null=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, null=True)
    etiquetas = models.CharField(max_length=255, blank=True, null=True)
    imagen = models.ImageField(null = True, upload_to="articulos")
    fecha_creacion = models.DateField(blank=True, null=True)
    fecha_publicacion = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.titulo #devuelvo el titulo del articulo

class Meta:
		db_table="articulos"
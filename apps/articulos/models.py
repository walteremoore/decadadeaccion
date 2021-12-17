from django.db import models
from apps.usuarios.models import Usuario
from apps.categorias.models import Categoria
from django.db import models
from tinymce import models as tinymce_models

class Etiqueta(models.Model):
    nombre = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table="etiquetas"
        ordering = ['nombre']

    def __str__(self):
        return self.nombre

ESTADOS_ARTICULO = (
    (1, "Artículo Activo"),
    (2, "Artículo Inactivo")
)

VISIBILIDAD_ARTICULO = (
    (1, "Visible - Publica"),
    (2, "Borrador - Privada")
)

class Articulo(models.Model):
    titulo = models.CharField(max_length=255, blank=True, null=True)
    contenido = tinymce_models.HTMLField()
    estado = models.IntegerField(choices=ESTADOS_ARTICULO, default=1)
    visibilidad = models.IntegerField(choices=VISIBILIDAD_ARTICULO, default=1)
    autor = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, null=True)
    etiquetas = models.ManyToManyField(Etiqueta)
    imagen = models.CharField(max_length=255, blank=True, null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True, blank=True)
    fecha_publicacion = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.titulo #devuelvo el titulo del articulo

    class Meta:
	    db_table="articulos"
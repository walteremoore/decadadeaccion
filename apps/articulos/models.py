from django.db import models
from apps.usuarios.models import Usuario
from apps.categorias.models import Categoria

class Etiqueta(models.Model):
    nombre = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table="etiquetas"
        ordering = ['nombre']

    def __str__(self):
        return self.nombre

class Articulo(models.Model):
    titulo = models.CharField(max_length=255, blank=True, null=True)
    contenido = models.TextField(blank=True, null=True)
    estado = models.BooleanField(blank=True, null=True, default=True) # True=visible, False=baja logica
    visibilidad = models.BooleanField(blank=True, null=True, default=False) # True=publicado, False=borrador
    autor = models.ForeignKey(Usuario, on_delete=models.CASCADE, null=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, null=True)
    etiquetas = models.ManyToManyField(Etiqueta)
    imagen = models.CharField(max_length=255, blank=True, null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True, blank=True)
    fecha_publicacion = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.titulo #devuelvo el titulo del articulo

    def publicar(self):
        self.visibilidad = True
        self.fecha_publicacion = date.today()

    def borrador(self):
        self.visibilidad = False

    def bajalogica(self):
        self.estado = False        

    class Meta:
	    db_table="articulos"
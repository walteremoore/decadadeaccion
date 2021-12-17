from django.db import models
from tinymce import models as tinymce_models

class Categoria(models.Model):
    nombre = models.CharField(max_length=255, blank=True, null=True)
    descripcion = tinymce_models.HTMLField()

    def __str__(self):
        return self.nombre
    
    class Meta:
	    db_table="categorias"


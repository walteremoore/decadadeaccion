from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    dni = models.IntegerField(null=True, blank=True)
    nombre = models.CharField(max_length=255, blank=True, null=True)
    apellido = models.CharField(max_length=255, blank=True, null=True)
    estado = models.BooleanField(blank=True, null=True)
    email = models.EmailField(max_length=254, blank=True, null=True)
    telefono = models.CharField(max_length=255, blank=True, null=True)
    direccion = models.CharField(max_length=255, blank=True, null=True)
    ciudad = models.CharField(max_length=255, blank=True, null=True)
    provincia = models.CharField(max_length=255, blank=True, null=True)
    pais = models.CharField(max_length=255, blank=True, null=True)
    foto = models.ImageField(null = True, blank=True, upload_to="images/")
    fecha_nacimiento = models.DateField(blank=True, null=True)

    class Meta:
        db_table="usuarios"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

from django.db import models
from django.contrib.auth.models import AbstractUser

ESTADO_USUARIOS = (
    (1, "Usuario Activo"),
    (2, "Usuario Inactivo - Bloqueado")
)

class Usuario(AbstractUser):
    dni = models.IntegerField(null=True, blank=True)
    estado = models.IntegerField(choices=ESTADO_USUARIOS, default=1)
    email = models.EmailField(max_length=254, blank=True, null=True)
    telefono = models.CharField(max_length=255, blank=True, null=True)
    direccion = models.CharField(max_length=255, blank=True, null=True)
    ciudad = models.CharField(max_length=255, blank=True, null=True)
    provincia = models.CharField(max_length=255, blank=True, null=True)
    pais = models.CharField(max_length=255, blank=True, null=True)
    foto = models.CharField(max_length=255, blank=True, null=True)
    fecha_nacimiento = models.DateField(blank=True, null=True)
    es_administrador = models.BooleanField(default=False) #True=usuario_admin, False=usuario_escritor

    class Meta:
        db_table="usuarios"


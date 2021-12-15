from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    dni = models.IntegerField(null=True, blank=True)
    estado = models.BooleanField(blank=True, null=True, default=True) #True=usuario_no_bloqueado, False=usuario_bloqueado
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

    def bloquear(self): #baja_logica
        self.estado = False

    def desbloquear(self): #usuario_no_bloqueado
        self.estado = True

    def hacer_admin(self): #usuario_admin
        self.es_administrador = True

    def quitar_admin(self): #usuario_escritor
        self.es_administrador = False

from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):
    # Campos adicionales si los necesitas
    telefono = models.CharField(max_length=20, blank=True, null=True)
    direccion = models.TextField(blank=True, null=True)
    es_administrador = models.BooleanField(default=False)
    es_voluntario = models.BooleanField(default=False)

    def __str__(self):
        return self.username

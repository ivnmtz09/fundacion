from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

class Usuario(AbstractUser):
    TIPOS_USUARIO = [
        ('ADMIN', 'Administrador'),
        ('STAFF', 'Staff Fundación'),
        ('VOLUNTARIO', 'Voluntario'),
        ('BENEFICIARIO', 'Beneficiario'),
    ]
    
    tipo_usuario = models.CharField(max_length=12, choices=TIPOS_USUARIO, default='VOLUNTARIO')
    telefono = models.CharField(max_length=15, blank=True, null=True)
    direccion = models.TextField(blank=True, null=True)
    fecha_nacimiento = models.DateField(blank=True, null=True)
    activo = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
    
    def __str__(self):
        return f"{self.get_full_name()} ({self.username})"
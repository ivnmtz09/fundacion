from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario

@admin.register(Usuario)
class UsuarioAdmin(UserAdmin):
    model = Usuario
    list_display = ('username', 'email', 'first_name', 'last_name', 'tipo_usuario', 'is_staff')
    fieldsets = UserAdmin.fieldsets + (
        ('Información adicional', {
            'fields': ('tipo_usuario', 'telefono', 'direccion', 'fecha_nacimiento', 'activo')
        }),
    )

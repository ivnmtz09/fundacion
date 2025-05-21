# usuarios/urls.py
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import (
    RegistroUsuarioAPIView,
    LoginUsuarioAPIView,
    PerfilUsuarioView,
    EditarPerfilUsuarioAPIView,
    CambiarContrasenaAPIView,
    vista_protegida,
)

urlpatterns = [
    path('auth/registro/', RegistroUsuarioAPIView.as_view(), name='registro'),
    path('auth/login/', LoginUsuarioAPIView.as_view(),  name='login'),
    path('auth/token/', TokenObtainPairView.as_view(),  name='token_obtain_pair'),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('auth/perfil/', PerfilUsuarioView.as_view(), name='perfil_usuario'),
    path('auth/perfil/editar/', EditarPerfilUsuarioAPIView.as_view(), name='editar_perfil'),
    path('auth/cambiar-contrasena/', CambiarContrasenaAPIView.as_view(), name='cambiar_contrasena'),
    path('protegido/', vista_protegida, name='vista_protegida'),
]

from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import Usuario
from rest_framework_simplejwt.tokens import RefreshToken

class UsuarioRegistroSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = Usuario
        fields = ['id', 'username', 'email', 'password', 'first_name', 'last_name', 'telefono', 'direccion']

    def validate_username(self, value):
        if Usuario.objects.filter(username=value).exists():
            raise serializers.ValidationError("El nombre de usuario ya está en uso.")
        return value

    def validate_email(self, value):
        if Usuario.objects.filter(email=value).exists():
            raise serializers.ValidationError("El correo ya está en uso.")
        return value

    def create(self, validated_data):
        user = Usuario(
            username=validated_data['username'],
            email=validated_data.get('email'),
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', ''),
            telefono=validated_data.get('telefono'),
            direccion=validated_data.get('direccion'),
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class UsuarioLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(username=data['username'], password=data['password'])
        if not user or not user.is_active:
            raise serializers.ValidationError("Credenciales inválidas")

        refresh = RefreshToken.for_user(user)
        return {
            'id': user.id,
            'username': user.username,
            'email': user.email,
            'access': str(refresh.access_token),
            'refresh': str(refresh),
        }

class UsuarioPerfilSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['first_name', 'last_name', 'email', 'telefono', 'direccion']

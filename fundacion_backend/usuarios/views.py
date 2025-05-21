from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from .serializers import UsuarioRegistroSerializer, UsuarioLoginSerializer, UsuarioPerfilSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes

class RegistroUsuarioAPIView(APIView):
    def post(self, request):
        serializer = UsuarioRegistroSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'mensaje': 'Usuario registrado correctamente'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginUsuarioAPIView(APIView):
    def post(self, request):
        serializer = UsuarioLoginSerializer(data=request.data)
        if serializer.is_valid():
            return Response(serializer.validated_data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PerfilUsuarioView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        usuario = request.user
        return Response({
            "id": usuario.id,
            "nombre": usuario.first_name,
            "apellido": usuario.last_name,
            "email": usuario.email,
            "es_activo": usuario.is_active,
        })

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def vista_protegida(request):
    return Response({"mensaje": f"Hola, {request.user.username}!"})

class EditarPerfilUsuarioAPIView(generics.RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UsuarioPerfilSerializer

    def get_object(self):
        return self.request.user
    
class CambiarContrasenaAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        usuario = request.user
        actual = request.data.get("actual")
        nueva = request.data.get("nueva")

        if not usuario.check_password(actual):
            return Response({"error": "La contraseña actual es incorrecta"}, status=400)

        usuario.set_password(nueva)
        usuario.save()
        return Response({"mensaje": "Contraseña actualizada correctamente"})

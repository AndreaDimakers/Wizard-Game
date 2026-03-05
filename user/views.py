from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from django.db import IntegrityError
from django.shortcuts import render, redirect
from django.contrib import messages
from.serializers import CrearUserSerializer, UserSerializer
from .service import CrearUsuario

class RegistroViews(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = CrearUserSerializer(data=request.data)
        if serializer.is_valid():
            try:
                user = CrearUsuario(
                    username=serializer.validated_data['usernamme'],
                    password=serializer.validated_data['password'],
                    acatar=serializer.validated_data('avatar', None)
                )

            except IntegrityError:
                return Response(
                    {"error": "El Username ya existe."},
                    status=status.HTTP_409_CONFLICT
                )

            response_serializer = UserSerializer(user)
            return Response(
                response_serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)             

                
# Create your views here.

def pagina_registro(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        avatar = request.POST.get('avatar')

        if password != confirm_password:
            messages.error(request, "Las contrasenas no coinciden.")
            return render(request, 'user/registro.html')
        
        try:

            user = CrearUsuario(
                username=username,
                password=password,
                avatar=avatar
            )

            messages.success(request, "Registro Exitoso!")
            
        except IntegrityError:

            messages.error(request, "El usuario ya existe.")
            return render(request, 'user/registro.html')
    
    return render(request, 'user/registro.html')
        




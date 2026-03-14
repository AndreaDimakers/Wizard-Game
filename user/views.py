from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from django.db import IntegrityError
from django.shortcuts import render, redirect
from django.contrib import messages
from.serializers import CrearUserSerializer, UserSerializer
from .uso import registrar_usuario
from .utils import Avatars

class RegistroViews(APIView):
    
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = CrearUserSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = registrar_usuario(
                username=serializer.validated_data['username'],
                password=serializer.validated_data['password'],
                avatar=serializer.validated_data.get('avatar', None)
            )

            response_serializer = UserSerializer(user)
            return Response(response_serializer.data,status=status.HTTP_201_CREATED)

        except ValueError as e:
            return Response(
                {"error": str(e)},status=status.HTTP_409_CONFLICT)


                     

            
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

            user = registrar_usuario(
                username=username,
                password=password,
                avatar=avatar
            )

            messages.success(request, "Registro Exitoso!")
            
        except ValueError as e:
            messages.error(request, str(e))
            return render(request, 'user/registro.html')
    
    return render(request, 'user/registro.html',{ 'avatars': Avatars.choices })
        




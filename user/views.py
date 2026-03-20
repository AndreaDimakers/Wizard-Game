from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from.serializers import CrearUserSerializer, UserSerializer, LogInSerializer
from .uso import registrar_usuario, login_usuario
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
            return redirect('login')
            
        except ValueError as e:
            messages.error(request, str(e))
            return render(request, 'user/registro.html')
    
    return render(request, 'user/registro.html',{ 'avatars': Avatars.choices })
        

class LoginViews(APIView):

    permission_classes=[AllowAny]

    def post(self, request):
        
        serializer = LogInSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        try: 
            user, tokens = login_usuario(
                username=serializer.validated_data['username'],
                password=serializer.validated_data['passowrd']
            )

            response_serializer = UserSerializer(user)

            return Response({
                "user": response_serializer.data,
                "tokens": tokens
            }, status=status.HTTP_200_OK)
        
        except ValueError as e:
            return Response({"error":str(e)}, status=status.HTTP_401_UNAUTHORIZED) 
        
def pagina_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user, tokens = login_usuario(username=username,password=password)

            login(request, user)
            messages.success(request,f"Sesion Iniciada")
            return redirect('home')
        
        except ValueError as e:
            messages.error(request, str(e))
            return render(request, 'user/login.html')
    
    return render(request, 'user/login.html')

class LogoutViews(APIView):

    def post(self,request):
        try:
            from rest_framework_simplejwt.tokens import RefreshToken

            refresh_token = request.data.get('refresh')
            token = RefreshToken(refresh_token)
            token.blacklist()

            return Response({"message": "Has cerrado sesion"}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)            


def pagina_logout(request):
    logout(request)
    messages.success(request, "Has cerrado sesion")
    return redirect('login')

@login_required(login_url='login')
def pagina_inicio(request):

    return render(request, 'user/home.html', {'user': request.user})
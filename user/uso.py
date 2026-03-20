from django.db import transaction
from user.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from .repositorio import get_username, crear_usuario, autenticar_usuario

def registrar_usuario(username,password,avatar):

    usuario_existe = get_username(username)

    if usuario_existe:
        raise ValueError("El Usuario ya existe.")
    
    if len(password) < 8:
        raise ValueError("La contrasena debe de tener al menos 8 caracteres.")
    
    create_user = crear_usuario(username,password,avatar)

    return create_user


def login_usuario(username, password):

    user = autenticar_usuario(username,password)

    if user is None:
        raise ValueError("You shall not pass")
    
    refresh = RefreshToken.for_user(user)
    tokens = {
        'refresh': str(refresh),
        'acces': str(refresh.access_token)
    }
    return user,tokens
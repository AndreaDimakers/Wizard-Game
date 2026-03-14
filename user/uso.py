from django.db import transaction
from user.models import User
from .repositorio import get_username, crear_usuario

def registrar_usuario(username,password,avatar):

    usuario_existe = get_username(username)

    if usuario_existe:
        raise ValueError("El Usuario ya existe.")
    
    if len(password) < 8:
        raise ValueError("La contrasena debe de tener al menos 8 caracteres.")
    
    create_user = crear_usuario(username,password,avatar)

    return create_user
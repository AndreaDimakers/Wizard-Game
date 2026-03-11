from django.db import transaction
from user.models import User
from .repositorio import get_username, crear_usuario

def registrar_usuario(username,password,avatar):

    usuario_existe = get_username(username)

    if usuario_existe:
        raise ValueError("El Usuario ya existe.")
    
    user = User(username=username,password=password,avatar=avatar)

    with transaction.atomic():
        create_user = crear_usuario(user)
    return create_user
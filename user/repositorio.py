from django.db import transaction
from user.models import User

def crear_usuario(username,password,avatar):
    with transaction.atomic():
        usuario = User.objects.create_user(username=username, password=password, avatar=avatar)
    return usuario

def get_username(username):
    return User.objects.filter(username=username).first()
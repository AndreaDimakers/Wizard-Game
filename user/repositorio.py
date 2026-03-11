from django.db import transaction
from user.models import User

def crear_usuario(user):
    with transaction.atomic():
        usuario = User.objects.create_user(user)
    return usuario

def get_username(username):
    return User.objects.filter(username=username).first()
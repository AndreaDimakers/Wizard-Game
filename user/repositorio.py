from django.db import transaction
from user.models import User
from django.contrib.auth import authenticate

def crear_usuario(username,password,avatar):
    with transaction.atomic():
        usuario = User.objects.create_user(username=username, password=password, avatar=avatar)
    return usuario

def get_username(username):
    return User.objects.filter(username=username).first()

 
def autenticar_usuario(username,password):
    user = authenticate(username=username, password=password)
    return user 
from django.db import transaction
from user.models import User

def CrearUsuario(username,password,avatar):
    with transaction.atomic():
        user = User.objects.create_user(
            username=username,
            password=password,
            avatar=avatar or User.Avatars.DEFAULT
        )
    return user
from django.db import transaction
from models import MatchRoom, Jugador
import string
import secrets

def generar_codigo(lenght=8):
    alphabet = string.ascii_uppercase + string.digits
    return ''.join(secrets.choice(alphabet) for _ in range(lenght)) 

def crear_match_room(nombre_room, creator_user):
    with transaction.atomic():
        
        codigo = generar_codigo()
            
        room = MatchRoom.objects.get_or_create(
            nombre_room=nombre_room,
            codigo=codigo
        )

        Jugador.objects.create(
            room=room,
            user = creator_user
            #turno
        )
    return room

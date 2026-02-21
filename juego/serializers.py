from rest_framework import serializers
from .models import MatchRoom, Jugador, Encantos
from user.models import User

class MatchRoomSerializer(serializers.ModelSerializer):

    class Meta:
        model = MatchRoom
        fields = [
            "id","status","nombre_room",
            "codigo","ganador","creado"
        ]


class JugadorSerializer(serializers.ModelSerializer):

    class Meta:

        username = serializers.CharField(source=user.username, read_only=True)

        model = Jugador
        fields = [
            "room","user","hp",
            "mana","turno"
        ]

class EncantosSerializer(serializers.ModelSerializer):

    class Meta:

        model = Encantos
        fields = [
            "nombre","daño","costo_mana"
            "tipo_encanto"
        ]
from rest_framework import serializers
from .models import MatchRoom, Jugador, Encantos


class MatchRoomSerializer(serializers.ModelSerializer):

    class Meta:
        model = MatchRoom
        fields = [
            "id","status","nombre_room",
            "codigo","ganador","creado"
        ]

class CrearMatchRoomSerializer(serializers.Serializer):

    nombre_room = serializers.CharField()


class JugadorSerializer(serializers.ModelSerializer):

    username = serializers.CharField(source="user.username", read_only=True)

    class Meta:

        model = Jugador
        fields = [
            "id","room","user","hp",
            "mana","turno","username"
        ]

class EncantosSerializer(serializers.ModelSerializer):

    class Meta:

        model = Encantos
        fields = [
            "nombre","daño","costo_mana",
            "tipo_encanto"
        ]
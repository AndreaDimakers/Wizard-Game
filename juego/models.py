from django.conf import settings
from django.db import models
from juego.utils import StatusPartida

class MatchRoom(models.Model):

    status = models.CharField(
        max_length=20,
        choices=StatusPartida.choices,
        default=StatusPartida.ESPERA
    )

    nombre_room = models.CharField(max_length=255)

    codigo = models.CharField(max_length=8, unique=True)

    ganador = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="ganador_room"
    )

    creado = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre} ({self.codigo})"


class Jugador(models.Model):

    room = models.ForeignKey(
        MatchRoom,
        on_delete=models.CASCADE,
        related_name="players"
    )

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    hp = models.IntegerField(default=100)

    mana = models.IntegerField(default=100)

    turno = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.user.username} in {self.room.codigo}"

class Encantos(models.Model):

    nombre = models.CharField(max_length=50)

    daño = models.IntegerField(default=0)

    costo_mana = models.IntegerField(default=0)

    curacion = models.IntegerField(default=0)

    tipo_encanto = models.CharField(max_length=15)
    
    def __str__(self):
    
        return self.nombre
    

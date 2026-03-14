from django.db import models

class StatusPartida(models.TextChoices):
        
        ESPERA = "espera", "Esperando a un jugador"
        ACTIVO = "activo", "Juego en curso"
        TERNINADO = "terminado", "Partida terminado"

class TipoEncanto(models.TextChoices):

        ATAQUE = "ataque", "Ataque"
        CURACION = "curacion", "Curacion"

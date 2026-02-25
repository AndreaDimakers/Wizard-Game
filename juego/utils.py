from django.db import models

class StatusPartida(models.TextChoices):
        
        ESPERA = "espera", "Esperando a un jugador"
        ACTIVO = "activo", "Juego en curso"
        TERNINADO = "terminado", "Juego terminado"




class Encantos(models.TextChoices):

        FUEGO = "fuego", "Fuego"
        HIELO = "hielo", "Hielo"
        
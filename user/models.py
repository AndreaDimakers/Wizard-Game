from django.contrib.auth.models import AbstractUser
from django.db import models
from user.utils import Avatars

class User(AbstractUser):

    avatar = models.ImageField(
        max_length=20,
        choices=Avatars.choices,
        default=Avatars.HARRY 
        )

    wins=models.IntegerField(default=0)

        
    
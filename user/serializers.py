from rest_framework import serializers
from .models import User
from .utils import Avatars

class UserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(
        write_only=True,
        required=False,
        style={"input_type": "password"}
    )

    class Meta:

        model = User
        fields = [
            "id","username","password",
            "avatar","wins","loses"
        ]

class CrearUserSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=20)
    password = serializers.CharField(write_only=True,min_length=8)
    avatar = serializers.ChoiceField(choices=Avatars.choices)

    #esto debera ir en una capa de validacion
    def validate_username(self,value):
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError("El Username ya existe.")
        
        return value

    
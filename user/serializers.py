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
            "avatar","wins"
        ]

class CrearUserSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)
    avatar = serializers.ChoiceField(choices=Avatars.choices)
    
from typing import Any, Dict

from rest_framework import serializers

from accounts.services import (
    get_user_from_oauth, 
    verify_google_jwt
)
from accounts.models import User

from rest_framework_simplejwt.serializers import TokenObtainSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from djoser.serializers import UserCreateSerializer


class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ("id", "email", "name", "password")


class GoogleAuthSerializer(TokenObtainSerializer):
    token_class = RefreshToken
    token = serializers.CharField()

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.fields[self.username_field] = serializers.CharField(
            required=False, allow_blank=True
        )
        self.fields["password"] = serializers.CharField(
            required=False, allow_blank=True
        )

    def validate(self, attrs: Dict[str, Any]) -> Dict[str, str]:
        user_data = verify_google_jwt(
            attrs.get("token")
        )

        if not user_data:
            raise serializers.ValidationError({'token': 'google did not confirm the token'})

        instance = get_user_from_oauth(user_data)

        refresh = self.get_token(instance)
        
        tokens = {
            "refresh": str(refresh),
            "access": str(refresh.access_token),
        }

        return tokens

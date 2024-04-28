from typing import Any
from faker import Faker

from django.contrib.auth import get_user_model
from djoser.signals import user_activated

from accounts.models import User


def get_user_from_oauth(user_data: dict[str, Any]) -> User:
    user_model = get_user_model()

    try:
        return user_model.objects.get(email=user_data['email'])

    except:
        user = user_model.objects.create_user(
            name=user_data['name'],
            email=user_data['email'],
            is_active=True,
            password=Faker().password(30)
        )
        user_activated.send(sender='get_user_from_oauth', user=user)
        return user

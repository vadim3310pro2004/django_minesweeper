from accounts.models import User
from minesweeper.models import Player


def create_player(user: User, *args, **kwargs) -> Player:
    return Player.objects.get_or_create(user=user)
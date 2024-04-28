from djoser.signals import user_activated

from minesweeper.services import create_player


user_activated.connect(create_player)

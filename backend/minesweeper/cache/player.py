from .base import BaseCache
from minesweeper.constants import PLAYER_CACHE


class CashedPlayer(BaseCache):
    """
    Cache for minesweeper_player
    """

    cache_alias = PLAYER_CACHE["NAME_SPACE"]
    cache_time = PLAYER_CACHE["TIME"]

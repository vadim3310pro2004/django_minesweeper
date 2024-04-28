from django.shortcuts import get_object_or_404
from minesweeper.models import Player


def get_top_scores(player_id: int, *args, **kwargs) -> str:
    """
    Return stringfy list (json) with top 5 scores
    """

    return get_object_or_404(
        Player.objects.only("top_5_scores"), id=player_id
    ).top_5_scores

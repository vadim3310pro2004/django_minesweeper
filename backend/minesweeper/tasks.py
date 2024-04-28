from typing import Optional
from logging import getLogger

from django.core.exceptions import ObjectDoesNotExist

from backend.celery import app
from minesweeper.models.player import Player
from minesweeper.services import add_new_success_score


logger = getLogger(__name__)


@app.task
def add_new_resoult_to_player(id: int, time: Optional[int] = None):
    try:
        instance = Player.objects.get(id=id)
    except ObjectDoesNotExist:
        logger.warning('player does not exist')
        return

    if time:
        instance = add_new_success_score(instance, time, False)

    instance.total_games += 1
    instance.save()

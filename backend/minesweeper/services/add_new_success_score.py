from minesweeper.models import Player


def add_new_success_score(
    instance: Player,
    new_score: int,
    save: bool = True,
    *args,
    **kwargs
) -> Player:
    """
    * updates top_5_scores
    * updates averange_resoult
    """
    # update top_5_scores
    if len(instance.top_5_scores) < 5:
        instance.top_5_scores = sorted(
            instance.top_5_scores + [new_score]
        )
    elif instance.top_5_scores[-1] > new_score:
        instance.top_5_scores = sorted(
            instance.top_5_scores + [new_score]
        )[0:5]

    instance.success_games += 1

    # Calculate new arefmetic men from all success games
    if (instance.averange_resoult):
        instance.averange_resoult = (
            instance.success_games * instance.averange_resoult + new_score
        ) / (
            instance.success_games + 1
        )
    else:
        instance.averange_resoult = new_score

    if save:
        instance.save()

    return instance

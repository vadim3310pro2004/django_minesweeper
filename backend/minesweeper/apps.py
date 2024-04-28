from django.apps import AppConfig


class MinesweeperConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'minesweeper'

    def ready(self) -> None:
        import minesweeper.signals_handlers
        return super().ready()
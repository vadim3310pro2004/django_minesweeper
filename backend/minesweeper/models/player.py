from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _


class Player(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        verbose_name=_("User"),
        related_name="player",
        on_delete=models.CASCADE,
    )
    total_games = models.PositiveIntegerField(
        verbose_name=_("Total games"), 
        default=0,
    )
    success_games = models.PositiveIntegerField(
        verbose_name=_('Success games'),
        default=0,
    )
    top_5_scores = models.JSONField(
        verbose_name=_("Best five resoults"), 
        default=list,
        blank=True,
    )
    averange_resoult = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name=_("Averange game time"),
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name_plural = _("Players")
        verbose_name = _("Player")

    def __str__(self) -> str:
        return f"<Player {self.user}>"

    def delete(self, *args, **kwargs):
        return super().delete(*args, **kwargs)

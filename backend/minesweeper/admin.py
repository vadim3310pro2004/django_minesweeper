from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from minesweeper.models import Player


admin.site.register(Player)

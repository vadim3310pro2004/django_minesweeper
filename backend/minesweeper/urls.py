from django.urls import include, path
from minesweeper.views import (
    PlayersView,
)

from rest_framework.routers import DefaultRouter

app_name = "minesweeper"


router = DefaultRouter()
router.register("players", PlayersView, basename="players")


urlpatterns = [
    path('api/v1/', include(router.urls)),
]

from rest_framework import serializers

from minesweeper.tasks import add_new_resoult_to_player
from minesweeper.models import Player
from minesweeper.cache import CashedPlayer


class PlayersSerializer(serializers.ModelSerializer):
    user_name = serializers.SerializerMethodField()

    def get_user_name(self, request):
        return request.user.name

    class Meta:
        model = Player
        fields = (
            "total_games", 
            "user",
            "top_5_scores",
            "user_name",
            "success_games",
            "averange_resoult",
        )

    def update(self, instance, validated_data, *args, **kwargs):
        add_new_resoult_to_player.delay(
            instance.id, 
            self.context.get("request").data.get("time")
        )
        return instance

    def save(self, *args, **kwargs):
        # Invalidate cache
        if id := self.context.get("request").user.id:
            CashedPlayer.invalidate(id)

        return super().save(**kwargs)

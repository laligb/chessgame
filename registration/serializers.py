from rest_framework import serializers

from .models import Player

class PlayerSerializer(serializers.ModelSerializer):

    # To extraxt username from player I need to use this method:
    player_username = serializers.SerializerMethodField()

    class Meta:
        model = Player
        fields = ('id', 'player_username', 'rating', 'games_played', 'games_won', 'games_lost', 'games_draw')

    # To get player username:
    def get_player_username(self, object):
        return object.player.username

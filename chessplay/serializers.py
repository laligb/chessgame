from rest_framework import serializers
from .models import Game

class GameSerializer(serializers.ModelSerializer):
    player_white = serializers.SerializerMethodField()
    player_black = serializers.SerializerMethodField()

    class Meta:
        model = Game
        fields = ("id", "white_player_id", "black_player_id", "player_white", "player_black", "moves", "result", "status", "date_played")

    def get_player_white(self, obj):
        return obj.white_player_id.player.username if obj.white_player_id.player else None

    def get_player_black(self, obj):
        return obj.black_player_id.player.username if obj.black_player_id.player else None

from rest_framework import serializers

from .models import Player

class PlayerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Player
        fields = ('id', 'rating', 'games_played', 'games_won', 'games_lost', 'games_draw')

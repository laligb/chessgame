from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Game, PlayerGameHistory
from registration.models import Player

# UPDATING PLAYER INFORMATION FROM FINISHED GAME
@receiver(post_save, sender=Game)
def update_statisticts(sender, instance, created, **kwargss):
    if instance.status == "finished":
        player1_history = PlayerGameHistory.objects.create(
            player = instance.white_player_id,
            opponent = instance.black_player_id,
            game = instance,
        )
        player2_history = PlayerGameHistory.objects.create(
            player = instance.black_player_id,
            opponent = instance.white_player_id,
            game = instance,
        )

        instance.white_player_id.update_statistics("white", instance.result, instance.black_player_id.rating)
        instance.black_player_id.update_statistics("black", instance.result, instance.white_player_id.rating)

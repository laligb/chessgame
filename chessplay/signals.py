from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Game
from registration.models import Player

# UPDATING PLAYER INFORMATION FROM FINISHED GAME
@receiver(post_save, sender=Game)
def update_statisticts(sender, instance, **kwargs):
    pass

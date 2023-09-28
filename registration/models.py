from django.db import models
from django.contrib.auth.models import User

class Player(models.Model):
    player = models.OneToOneField(User, on_delete=models.CASCADE)
    rating = models.IntegerField(default=1000)
    games_played = models.IntegerField(default=0)
    games_won = models.IntegerField(default=0)
    games_lost = models.IntegerField(default=0)
    games_draw = models.IntegerField(default=0)
    #opponents = models.ManyToManyField('self', through="Game",symmetrical=True)

    def __str__(self):
       return self.player.username

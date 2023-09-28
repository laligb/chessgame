from django.db import models
from registration.models import Player

class Game(models.Model):

    white_player_id = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='white_player')
    black_player_id = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='black_player')
    moves = models.TextField() # PGN format

    result = models.CharField(max_length=10, choices=["1:0", "0:1", "1/2-1/2", "-:-", "+:-", "-:+"], default="-:-")
    status = models.CharField(max_length=10, choices=["not started", "ongoing", "finished"], default='not started')
    date_played = models.DateTimeField(auto_now_add=True)
    winner = models.IntegerField()

    def __str__(self):
        return f"Game between {self.white_player.user.username} and {self.black_player.user.username}, result: "

    def set_result(self, game_result):
        self.result = game_result

        if game_result == "-:-":
            return "not result"

        self.white_player.game_played += 1
        self.black_player.game_played += 1

        if game_result == "1:0" or game_result == "+:-":
            self.white_player.game_won += 1
            self.black_player.game_lost += 1
        elif game_result == "0:1" or game_result == "-:+":
            self.white_player.game_lost += 1
            self.black_player.game_won += 1
        elif game_result == "1/2-1/2":
            self.white_player.game_draw += 1
            self.black_player.game_draw += 1
        else:
            self.white_player.game_lost += 0
            self.black_player.game_lost += 0


        self.white_player.save()
        self.black_player.save()
        self.save()

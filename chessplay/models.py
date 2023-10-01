from django.db import models
# from registration.models import Player


class Game(models.Model):

    # white_player_id = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='white_player')
    # black_player_id = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='black_player')
    white_player_id = models.ForeignKey('registration.Player', on_delete=models.CASCADE, related_name='white_player')
    black_player_id = models.ForeignKey('registration.Player', on_delete=models.CASCADE, related_name='black_player')

    moves = models.TextField() # PGN format

    RESULT_CHOICES = [
        ("1:0", "1:0"),
        ("0:1", "0:1"),
        ("1/2-1/2", "1/2-1/2"),
        ("-:-", "-:-"),
        ("+:-", "+:-"),
        ("-:+", "-:+"),
    ]

    STATUS_CHOICES = [
        ("not started", "Not Started"),
        ("ongoing", "Ongoing"),
        ("finished", "Finished"),
    ]

    result = models.CharField(max_length=50, choices=RESULT_CHOICES, default="-:-")
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='not started')
    date_played = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"Game between {self.white_player_id.player.username} and {self.black_player_id.player.username},\
            result: {self.result}, status: {self.status}"

    def white_player(self):
        return self.white_player_id.player

    def black_player(self):
        return self.black_player_id.player


class PlayerGameHistory(models.Model):
    player = models.ForeignKey("registration.Player", on_delete=models.CASCADE, related_name='player1')
    opponent = models.ForeignKey("registration.Player", on_delete=models.CASCADE, related_name="opponent_history")
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='games_played')

    class Meta:
        unique_together = ('player', 'game')

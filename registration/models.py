from django.db import models
from django.contrib.auth.models import User

class Player(models.Model):
    player = models.OneToOneField(User, on_delete=models.CASCADE)
    rating = models.IntegerField(default=1000)
    games_played = models.IntegerField(default=0)
    games_won = models.IntegerField(default=0)
    games_lost = models.IntegerField(default=0)
    games_draw = models.IntegerField(default=0)


    def __str__(self):
       return f"Player: {self.player.username}, rating: {self.rating}, games amount {self.games_played}, \
         wins: {self.games_won}, lost: {self.games_lost}, draw: {self.games_draw}"

    # UPDATE STATISTICS AND RATING OF PLAYER
    # New Rating (R_new) = Old Rating (R_old) + K × (Result - Expected Result)
    # Lets Assume that K = 20 for this app
    # Expected Result = 1 / (1 + 10^((R_opponent - R_player) / 400))

    def update_statistics(self, player_color, result, rating_of_opponent):
        self.games_played += 1
        K = 20
        expected_result = 1 / (1 + 10**((rating_of_opponent - self.rating)/ 400))

        if result == "1/2-1/2":
            self.games_draw += 1
            self.rating =  int(self.rating + K * (0.5 - expected_result))

        if player_color == "white":
            if result == "1:0" or result == "+:-":
                self. games_won += 1
                self.rating =  int(self.rating + K * (1 - expected_result))
            elif result == "0:1":
                self.games_lost += 1
                self.rating =  int(self.rating + K * (0 - expected_result))

        elif player_color == "black":
            if result == "0:1" or result == "-:+":
                self.games_won += 1
                self.rating =  int(self.rating + K * (1 - expected_result))
            elif result == "1:0":
                self.games_lost += 1
                self.rating =  int(self.rating + K * (0 - expected_result))


        self.save()

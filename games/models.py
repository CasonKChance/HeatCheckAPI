from django.db import models
from users.models import User
from courts.models import Court


class GameManager(models.Manager):
    def get_games_for_user(self, user_id):
        return self.filter(players_associated__playerID=user_id)


class Game(models.Model):
    gameID = models.AutoField(primary_key=True)
    court = models.ForeignKey(
        Court, on_delete=models.CASCADE, related_name='games')
    players_associated = models.ManyToManyField(User, related_name='games')

    objects = GameManager()

    def __str__(self):
        return f"Game {self.gameID} at {self.court.address}"

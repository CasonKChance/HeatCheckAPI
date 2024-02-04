from django.db import models
from users.models import User
from courts.models import Court


class Game(models.Model):
    gameID = models.AutoField(primary_key=True)
    court = models.ForeignKey(
        Court, on_delete=models.CASCADE, related_name='games')
    players_associated = models.ManyToManyField(User, related_name='games')

    def __str__(self):
        return f"Game {self.gameID} at {self.court.address}"

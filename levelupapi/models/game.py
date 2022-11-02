from django.db import models

class Game(models.Model):

    game_type = models.ForeignKey('GameType', on_delete=models.CASCADE, related_name='game_type')
    gamer = models.ForeignKey('Gamer', on_delete=models.CASCADE, related_name='gamer')
    title = models.CharField(max_length=50)
    maker = models.CharField(max_length=50)
    number_of_players = models.IntegerField()
    skill_level = models.IntegerField()

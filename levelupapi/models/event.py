from django.db import models

class Event(models.Model):

    game = models.ForeignKey('Game', on_delete=models.CASCADE)
    description = models.CharField(max_length=500)
    date = models.DateField(auto_now=False, auto_now_add=False)
    time = models.TimeField(auto_now=False, auto_now_add=False)
    organizer = models.ForeignKey('Gamer', on_delete=models.CASCADE)
    gamers = models.ManyToManyField('Gamer', through='EventGamer', related_name='eventgamers')
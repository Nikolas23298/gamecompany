from django.db import models
from django.contrib.auth.models import User


class Game(models.Model):
    game_image = models.ImageField(null = True , blank = True, upload_to = "images/")
    TYPE_CHOICES = [('FPS','First Person Shooter'),('RPG','Role Playing Game'),('RTS','Real Time Strategy'),('SnS','Simulation and Sports')]
    title = models.CharField(max_length=50)
    description = models.TextField()
    types = models.CharField(max_length=3, choices=TYPE_CHOICES)
    release_date = models.DateTimeField(null=True)
    age = models.IntegerField()
    awards = models.ManyToManyField('Award', blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name="games")

    def __str__(self):
        return self.title

class Award(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


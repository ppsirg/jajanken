from django.db import models


class Player(models.Model):
    """Game Player."""
    name = models.CharField(max_length=100)
    won_matches = models.IntegerField(default=0)

    def __str__(self):
        return self.name

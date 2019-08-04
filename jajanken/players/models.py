from django.db import models


class Player(models.Model):
    """Game Player."""
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

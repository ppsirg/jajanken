from django.db import models
from players.models import Player
from .choices import JAJANKEN_CHOICES, JAJANKEN_BEAT_RULES


class MatchEvent(models.Model):
    """Game Player."""
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    choice = models.CharField(max_length=1, choices=JAJANKEN_CHOICES)
    match_round = models.ForeignKey('MatchRound', on_delete=models.CASCADE)

    def str_choice(self):
        """Show human friendly representation of choice.

        Returns
        -------
        str
            human friendly representation of choice.

        """
        return [a[1] for a in JAJANKEN_CHOICES if self.choice == a[0]][0]

    def __str__(self):
        return '{0.str_choice} {0.player.name}'.format(self)


class MatchRound(models.Model):
    """Match between two players, red one and blue one."""
    match = models.ForeignKey('Match', on_delete=models.CASCADE)

    def safe_getter(self, queryset):
        return queryset.last() if queryset.exists() else None

    def find_events(self):
        """Find events of players.

        Returns
        -------
        tuple
            return a tuple of red and blue events associated with current
            MatchRound, if any event doesnt exist, return None.

        """
        match_events = MatchEvent.objects.filter(match_round=self)
        blue = match_events.filter(player=self.match.blue_player)
        red = match_events.filter(player=self.match.red_player)
        return self.safe_getter(red), self.safe_getter(blue)

    def winner(self):
        """Calculate round winner.

        Returns
        -------
        Player
            return an instance of winer player, if there is not winer or match
            didnt finished, return None.

        """
        red_player_event, blue_player_event = self.find_events()
        if not all([red_player_event, blue_player_event]):
            # match round is not finished
            return None

        if red_player_event.choice == blue_player_event.choice:
            # there is a tie, no winner
            return None
        else:
            scenario = '{}_beats_{}'.format(
                red_player_event.choice, blue_player_event.choice
            )
            return red_player_event.player if scenario in JAJANKEN_BEAT_RULES else blue_player_event.player

    def __str__(self):
        winner = self.winner()
        return '{0}'.format(
            'even' if not winner else self.winner()
            )


class Match(models.Model):
    """Match between two Player."""
    red_player = models.ForeignKey(
        Player,
        related_name='red',
        on_delete=models.CASCADE
        )
    blue_player = models.ForeignKey(
        Player,
        related_name='blue',
        on_delete=models.CASCADE
        )
    rounds_per_match = 3

    def winner(self):
        """Calculate winner or match.

        Returns
        -------
        str
            return Player that won the match, if there is not a winner or
            match is not finished, return None.

        """
        rounds = MatchRound.objects.filter(match=self)
        if rounds.count() < self.rounds_per_match:
            # match is not finished
            return None

        winners = [round.winner() for round in rounds]
        winners = [a for a in winners if a is not None]

        if winners.count(self.blue_player) < winners.count(self.red_player):
            return self.red_player
        elif winners.count(self.blue_player) == winners.count(self.red_player):
            # there is a tie, not winner
            return None
        else:
            return self.blue_player

    def __str__(self):
        return ' and '.join([self.red_player, self.blue_player])


class PlayerStats(models.Model):
    """Player playing record."""
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    victories = models.IntegerField()
    defeats = models.IntegerField()
    ties = models.IntegerField()

    def __str__(self):
        return '{} won {} times'.format(self.player, self.victories)

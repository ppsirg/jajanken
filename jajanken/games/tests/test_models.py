# -*- coding: utf-8 -*-

# from django.test import TestCase

# Create your tests here.
import pytest
from games.models import *
from players.models import *


pytestmark = pytest.mark.django_db


class TestMatchModel():

    def test_tie(self):
        red, blue = self.build_players()
        response = self.factory(
            [red, blue],
            [['1', '1'], ['1', '1'], ['1', '1']]
            )
        assert response is None

    def test_red_win(self):
        red, blue = self.build_players()
        response = self.factory(
            [red, blue],
            [['1', '3'], ['1', '2'], ['1', '3']]
            )
        assert response == red

    def test_blue_win(self):
        red, blue = self.build_players()
        response = self.factory(
            [red, blue],
            [['1', '1'], ['1', '1'], ['1', '2']]
            )
        assert response == blue

    def test_not_finished_match(self):
        red, blue = self.build_players()
        response = self.factory(
            [red, blue],
            [['1', '3'], ['1', '2']],
            round_number=2
            )
        assert response is None

    def build_players(self):
        red = Player.objects.create(name='red_sox')
        blue = Player.objects.create(name='blue_sox')
        return red, blue

    def factory(self, players, sets, round_number=None):
        match = Match.objects.create(
            red_player=players[0],
            blue_player=players[1]
        )
        rounds = round_number if round_number else match.rounds_per_match
        for i in range(rounds):
            match_round = MatchRound.objects.create(
                match=match
            )
            red_event = MatchEvent.objects.create(
                player=match.red_player,
                choice=sets[i][0],
                match_round=match_round
            )
            blue_event = MatchEvent.objects.create(
                player=match.blue_player,
                choice=sets[i][1],
                match_round=match_round
            )
        return match.winner()

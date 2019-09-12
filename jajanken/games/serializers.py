# -*- coding: utf-8 -*-

from .models import MatchEvent, MatchRound, Match
from rest_framework import serializers


class MatchSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Match
        fields = ['id', 'blue_player', 'red_player']


class MatchRoundSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MatchRound
        fields = ['id', 'match']


class MatchEventSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MatchEvent
        fields = ['id', 'player', 'choice', 'match_round']

from .models import MatchEvent, MatchRound, Match
from rest_framework import serializers


class MatchSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Match
        fields = ['blue_player', 'red_player']


class MatchEventSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MatchEvent
        fields = ['choice', 'player', 'match_round']


class MatchRoundSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MatchRound
        fields = ['match']
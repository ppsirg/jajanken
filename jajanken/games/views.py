# -*- coding: utf-8 -*-
from django.views.generic import TemplateView, ListView
from .serializers import *
from rest_framework import viewsets
from .models import *


class JajankenView(TemplateView):
    template_name = 'app_template.html'


class ScoresView(TemplateView):
    template_name = 'score_list_template.html'

    def get_context_data(self):
        context = super().get_context_data()
        context['player_stats'] = [
            {'rank': 1, 'name': 'lol', 'won_matches': 12, 'lost_matches': 1},
            {'rank': 2, 'name': 'lol', 'won_matches': 12, 'lost_matches': 1},
            {'rank': 3, 'name': 'lol', 'won_matches': 12, 'lost_matches': 1},
            {'rank': 4, 'name': 'lol', 'won_matches': 12, 'lost_matches': 1},
        ]
        return context


class PlayerStatsViewSet(viewsets.ModelViewSet):
    """Rest-like view for Player model."""
    queryset = PlayerStats.objects.all()
    serializer_class = PlayerStatsSerializer


class MatchViewSet(viewsets.ModelViewSet):
    """Rest-like view for Match model."""
    queryset = Match.objects.all()
    serializer_class = MatchSerializer


class MatchEventViewSet(viewsets.ModelViewSet):
    """Rest-like view for MatchEvent model."""
    queryset = MatchEvent.objects.all()
    serializer_class = MatchEventSerializer


class MatchRoundViewSet(viewsets.ModelViewSet):
    """Rest-like view for MatchRound model."""
    queryset = MatchRound.objects.all()
    serializer_class = MatchRoundSerializer

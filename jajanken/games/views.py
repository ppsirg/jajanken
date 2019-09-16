# -*- coding: utf-8 -*-

from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.views.generic import TemplateView
from rest_framework import viewsets

from .serializers import *
from .models import *


class JajankenView(TemplateView):
    template_name = 'app_template.html'


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


def getMatchWinner(request, *args, **kwargs):
    """Get the id of match winner, can be red, blue or none for even match.

    Parameters
    ----------
    request : type
        Description of parameter `request`.
    *args : type
        Description of parameter `*args`.
    **kwargs : type
        Description of parameter `**kwargs`.

    Returns
    -------
    type
        JsonResponse with match winner id or none if even match.

    """
    match_obj = get_object_or_404(Match, pk=kwargs['match_id'])
    match_winner = match_obj.winner()
    if match_winner:
        match_winner.won_matches += 1
        match_winner.save()
    winner_id = match_winner.id if match_winner else None
    return JsonResponse({'winner': winner_id})


def getRoundWinner(request, *args, **kwargs):
    """Get the id of match winner, can be red, blue or none for even match.

    Parameters
    ----------
    request : type
        Description of parameter `request`.
    *args : type
        Description of parameter `*args`.
    **kwargs : type
        Description of parameter `**kwargs`.

    Returns
    -------
    type
        JsonResponse with match winner id or none if even match.

    """
    match_obj = get_object_or_404(MatchRound, pk=kwargs['match_round_id'])
    match_winner = match_obj.winner()
    winner_id = match_winner.id if match_winner else None
    return JsonResponse({'winner': winner_id})

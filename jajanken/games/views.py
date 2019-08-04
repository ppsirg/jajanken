# -*- coding: utf-8 -*-
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

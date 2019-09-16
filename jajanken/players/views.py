# -*- coding: utf-8 -*-
from rest_framework import viewsets
from rest_framework.views import APIView
from django.views.generic import ListView
from django.http import Http404
from .models import Player
from .serializers import PlayerSerializer
from rest_framework.response import Response
from rest_framework import status


class ScoresView(ListView):
    template_name = 'score_list_template.html'
    model = Player

    def get_ordering(self):
        return '-won_matches'


class PlayerViewSet(viewsets.ModelViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer

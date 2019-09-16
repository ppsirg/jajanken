# -*- coding: utf-8 -*-
from django.contrib import admin
from django.urls import path
from .views import JajankenView, getMatchWinner, getRoundWinner
from players.views import ScoresView


urlpatterns = [
    path('', JajankenView.as_view(), name='jajanken'),
    path('scores', ScoresView.as_view(), name='scores'),
    path('winner/<int:match_id>/', getMatchWinner, name='jajanken_winner'),
    path('winner_round/<int:match_round_id>/', getRoundWinner, name='jajanken_round_winner'),
]

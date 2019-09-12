# -*- coding: utf-8 -*-
from django.contrib import admin
from django.urls import path
from .views import JajankenView, getMatchWinner
from players.views import ScoresView


urlpatterns = [
    path('', JajankenView.as_view(), name='jajanken'),
    path('scores', ScoresView.as_view(), name='scores'),
    path('winner/<int:match_id>/', getMatchWinner, name='jajanken_winner'),
]

"""jajanken URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from players.views import PlayerViewSet
import games.views as game_view

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'players', PlayerViewSet)
router.register(r'matches', game_view.MatchViewSet)
router.register(r'match-rounds', game_view.MatchRoundViewSet)
router.register(r'match-events', game_view.MatchEventViewSet)

urlpatterns = [
    path('', include('games.urls')),
    # path('players/', include('players.urls')),
    path('api/', include(router.urls)),
]

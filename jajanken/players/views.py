# -*- coding: utf-8 -*-

from rest_framework import serializers, viewsets
from .models import Player


# Serializers define the API representation.
class PlayerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Player
        fields = ['name']

# ViewSets define the view behavior.
class PlayerViewSet(viewsets.ModelViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer

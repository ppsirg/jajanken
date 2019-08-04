# -*- coding: utf-8 -*-
from rest_framework import serializers
from .models import Player


class PlayerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Player
        fields = ['id', 'name', 'won_matches']
    # id = serializers.IntegerField(read_only=True)
    # name = serializers.CharField(max_length=100)
    # won_matches = serializers.IntegerField(read_only=True, required=False)
    #
    # def create(self, validated_data):
    #     return Player.objects.create(**validated_data)

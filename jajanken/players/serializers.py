# -*- coding: utf-8 -*-
from rest_framework import serializers
from .models import Player


class PlayerSerializer(serializers.Serializer):
    """Serialize Player Model."""
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100)
    won_matches = serializers.IntegerField(read_only=True, required=False)

    def create(self, validated_data):
        """Override create method to get uppercase of names"""
        validated_data['name'] = validated_data['name'].upper()
        return Player.objects.create(**validated_data)

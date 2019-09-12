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

# class PlayerListView(APIView):
#
#     def get(self, request, format=None):
#         snippets = Player.objects.all()
#
#         serializer = PlayerSerializer(snippets, many=True)
#         return Response(serializer.data)
#
#     def post(self, request, format=None):
#         serializer = PlayerSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# class PlayerDetailView(APIView):
#
#     def get_object(self, pk):
#         try:
#             return Player.objects.get(pk=pk)
#         except Player.DoesNotExist:
#             raise Http404
#
#     def get(self, request, pk, format=None):
#         player = self.get_object(pk)
#         serializer = PlayerSerializer(player)
#         return Response(serializer.data)
#
#     def put(self, request, pk, format=None):
#         player = self.get_object(pk)
#         serializer = PlayerSerializer(player, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, pk, format=None):
#         player = self.get_object(pk)
#         player.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

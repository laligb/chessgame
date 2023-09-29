from django.shortcuts import render, get_object_or_404
from django.views import generic
from chessplay.models import Game
from rest_framework import viewsets
from .serializers import GameSerializer

class IndexView(generic.ListView):
    template_name = "chessplay/index.html"
    context_object_name = "game_list"

    def get_queryset(self):
        """Return all games."""
        return Game.objects.all()


class GameView(viewsets.ModelViewSet):
    serializer_class = GameSerializer

    queryset = Game.objects.all()

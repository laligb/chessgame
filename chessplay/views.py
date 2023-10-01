from django.shortcuts import render, get_object_or_404
from django.views import generic
from chessplay.models import Game
from rest_framework import viewsets, pagination, mixins
from .serializers import GameSerializer
from rest_framework.permissions import IsAuthenticated


class IndexView(generic.ListView):
    template_name = "chessplay/index.html"
    context_object_name = "game_list"

    def get_queryset(self):
        """Return all games."""
        return Game.objects.all()


class GameView(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    serializer_class = GameSerializer
    queryset = Game.objects.all()
    permission_classes = [IsAuthenticated]
    # pagination_class = GamePagination

    def get_queryset(self):
        return Game.objects.all()

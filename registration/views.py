from django.shortcuts import render
from django.views import generic
from .models import Player
from .serializers import PlayerSerializer

class IndexView(generic.ListView):
    template_name = "registration/index.html"
    context_object_name = "player_list"

    serializer_class = PlayerSerializer

    def get_queryset(self):
        """Return all players."""
        return Player.objects.all()

class PlayerDetailView(generic.DetailView):
    model = Player
    template_name = 'registration/player_detail.html'
    context_object_name = 'player'

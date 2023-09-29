from django.shortcuts import render
from django.views import generic
from .models import Player
from .serializers import PlayerSerializer
from rest_framework import viewsets

class IndexView(generic.ListView):
    template_name = "registration/index.html"
    context_object_name = "player_list"

    def get_queryset(self):
        """Return all players."""
        return Player.objects.all()

class PlayerDetailView(generic.DetailView):
    model = Player
    template_name = 'registration/player_detail.html'
    context_object_name = 'player'


# create a class for the Todo model viewsets
class PlayerView(viewsets.ModelViewSet):

    # create a serializer class and assign
    serializer_class = PlayerSerializer

    # define a variable and populate it
    # with the Player list objects
    queryset = Player.objects.all()

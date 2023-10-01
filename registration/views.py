from django.shortcuts import render
from django.views import generic
from .models import Player
from .serializers import PlayerSerializer
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from rest_framework import generics


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
    serializer_class = PlayerSerializer
    queryset = Player.objects.all()

    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = User

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = User

from django.shortcuts import render, redirect
from django.views import generic
from .models import Player
from .serializers import PlayerSerializer
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django.contrib.auth.models import User
from rest_framework import generics
from .permisions import IsPlayerOrReadOnly, IsProfileOwnerOrAdmin

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

# VIEWSETS
class PlayerView(viewsets.ReadOnlyModelViewSet):
    serializer_class = PlayerSerializer
    queryset = Player.objects.all()

    authentication_classes = [SessionAuthentication, BasicAuthentication]
    #permission_classes = [IsPlayerOrReadOnly, IsAuthenticated]
    permission_classes = [IsAuthenticated]


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = User

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = User

# Registration with Forms
from .forms import RegistrationForm
from django.contrib.auth import login
def registration_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile')  # Redirect to the user's profile page
    else:
        form = RegistrationForm()
    return render(request, 'registration/register.html', {'form': form})

#Registration with rest api
# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework.decorators import api_view
# from django.contrib.auth import login
# from .serializers import UserRegistrationSerializer

# @api_view(['POST'])
# def register_user(request):
#     if request.method == 'POST':
#         serializer = UserRegistrationSerializer(data=request.data)
#         if serializer.is_valid():
#             user = serializer.save()
#             login(request, user)
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

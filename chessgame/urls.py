"""
URL configuration for chessgame project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from registration import views as player_views
from chessplay import views as game_views

from rest_framework import routers

router = routers.DefaultRouter()
router.register(r"players", player_views.PlayerView, 'players' )
router.register(r"games", game_views.GameView, "games")

urlpatterns = [
    path('chessplay/', include("chessplay.urls")),
    path('players/', include("registration.urls")),
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),

]

urlpatterns += [
    path('api/v1/', include('rest_framework.urls')),
]

from django.urls import path, include
from . import views

app_name = "registration"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path('player/<int:pk>/', views.PlayerDetailView.as_view(), name='player-detail'),
]

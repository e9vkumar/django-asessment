from django.urls import path
from .views import AllTeamView,DetailTeamView

urlpatterns = [
    path('teams/',AllTeamView.as_view(),name="all-view"),
    path('teams/<pk>/',DetailTeamView.as_view(),name="detail-view"),
]
from django.urls import path
from .views import AllTeamView,DetailTeamView

app_name = "tour"

urlpatterns = [
    path('teams/',AllTeamView.as_view(),name="all-view"),
    path('teams/<int:pk>/',DetailTeamView.as_view(),name="detail-view"),
]
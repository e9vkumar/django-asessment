from django.urls import path
import views
urlpatterns = [
    path('/teams/',views.AllTeamView.as_view(),name="all-view"),
    path('/teams/<team_name>/',views.DetailTeamView.as_view(),name="detail-view"),
]
from django.urls import path
import views
urlpatterns = [
    path('/teams/',views.AllTeamView.as_view(),name="all-view"),
    
]
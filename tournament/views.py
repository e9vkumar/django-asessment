from django.shortcuts import render
from django.views import generic
from .models import Team

# Create your views here.
class AllTeamView(generic.ListView):
    template_name = "team_list.html"
    def get_queryset(self):
        return Team.objects.all()
    

class DetailTeamView(generic.DetailView):
    model = Team
    
    


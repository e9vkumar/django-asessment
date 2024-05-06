from django.shortcuts import render
from django.views import generic
from .models import Team

# Create your views here.
class AllTeamView(generic.ListView):
    context_object_name = "teams"
    template_name = "team_list.html"
    def get_queryset(self):
        return Team.objects.all()
    

class DetailTeamView(generic.DetailView):
    model = Team
    context_object_name = "team"
    template_name = "team_view.html"

    def retrieve(request,pk):
        print(pk)
        return Team.objects.filter(id=pk)
    
    


from django.forms import forms
from .models import Match,TeamMatch

class MatchForm(forms.Form):
    class Meta:
        fields = "__all__"
        model = Match

class TeamMatchForm(forms.Form):
    class Meta:
        fields="__all__"
        model = TeamMatch


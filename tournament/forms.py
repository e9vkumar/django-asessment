from django.forms import forms
from .models import Match

class MatchForm(forms.Form):
    class Meta:
        fields = "__all__"
        model = Match



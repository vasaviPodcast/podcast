from .models import PodcastDetails
from django import forms

class AdminForm(forms.ModelForm):
    class Meta:
        model = PodcastDetails
        fields = "__all__"
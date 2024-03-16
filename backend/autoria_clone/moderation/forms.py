from django import forms
from .models import Moderation

class ModerationForm(forms.ModelForm):
    moderation_status = forms.ChoiceField(choices=Moderation.MODERATION_CHOICES)

    class Meta:
        model = Moderation
        fields = ['moderation_status']
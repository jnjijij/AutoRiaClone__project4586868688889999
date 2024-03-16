from django import forms
from .models import AdInfo

class AdInfoForm(forms.ModelForm):
    class Meta:
        model = AdInfo
        fields = ['title', 'description', 'price', 'image']
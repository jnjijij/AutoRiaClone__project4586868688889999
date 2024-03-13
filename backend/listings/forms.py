from django import forms
from models import Listing


class ListingForm(forms.ModelForm):
    class Meta:
        model = Listing
        fields = ['make', 'model', 'price', 'currency']

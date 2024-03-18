rom django import forms
from models import Car

class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['manufacturer', 'model', 'year', 'color']


class UserProfileForm:
    def save(self):
        pass

    def is_valid(self):
        pass

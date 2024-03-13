from django import forms
from models import Car, CarPrice

class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'

class CarPriceForm(forms.ModelForm):
    class Meta:
        model = CarPrice
        fields = '__all__'

from django import forms
from models import CarBrand, CarModel, CarPrice, User, Ad

class CarBrandForm(forms.ModelForm):
    class Meta:
        model = CarBrand
        fields = ['name']

class CarModelForm(forms.ModelForm):
    class Meta:
        model = CarModel
        fields = ['brand', 'name']

class CarPriceForm(forms.ModelForm):
    class Meta:
        model = CarPrice
        fields = ['car', 'currency', 'price']

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'account_type']

class AdForm(forms.ModelForm):
    class Meta:
        model = Ad
        fields = ['user', 'car', 'price', 'content']

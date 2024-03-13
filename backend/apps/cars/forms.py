from django import forms
from models import CarBrand, CarModel, CarPrice, User, Ad

class CarBrandForm(forms.ModelForm):
    class Meta:
        model = CarBrand
        fields = ['name']

class CarModelForm(forms.ModelForm):
    class Meta:
        model = CarModel
        fields = ['name', 'brand']

class CarPriceForm(forms.ModelForm):
    class Meta:
        model = CarPrice
        fields = ['price', 'model']

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'phone']

class AdForm(forms.ModelForm):
    class Meta:
        model = Ad
        fields = ['title', 'description', 'user', 'car_model', 'price']

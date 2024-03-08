from django import forms

class AutoPriceForm(forms.Form):
    title = forms.CharField(max_length=100)
    price = forms.DecimalField(max_digits=10, decimal_places=2)
    currency = forms.ChoiceField(choices=[('USD', 'USD'), ('EUR', 'EUR'), ('UAH', 'UAH')])
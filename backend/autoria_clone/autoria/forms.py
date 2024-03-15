from django import forms
from django.forms.utils import ErrorList


class AutoPriceForm(forms.Form):
    def __init__(self, data=None, files=None, auto_id='id_%s', prefix=None,
                 initial=None, error_class=ErrorList, label_suffix=None,
                 empty_permitted=False, field_order=None, use_required_attribute=None, renderer=None):
        super().__init__(data, files, auto_id, prefix, initial, error_class, label_suffix, empty_permitted, field_order,
                         use_required_attribute, renderer)
        self.instance = None

    title = forms.CharField(max_length=100)
    price = forms.DecimalField(max_digits=10, decimal_places=2)
    currency = forms.ChoiceField(choices=[('USD', 'USD'), ('EUR', 'EUR'), ('UAH', 'UAH')])
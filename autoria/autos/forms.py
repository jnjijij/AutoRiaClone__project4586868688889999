from django import forms
from django.contrib.auth.models import User
from .models import Auto, Autosalon, AutoImage, Report
from .models import Image
from django import forms
from .models import AutoImage

class AutoForm(forms.ModelForm):
    class Meta:
        model = Auto
        fields = ('name', 'model', 'price', 'currency', 'description', 'image')
        widgets = {
            'description': forms.Textarea(attrs={'rows': 5, 'cols': 40}),
            'image': forms.FileInput,
        }

class AutosalonForm(forms.ModelForm):
    class Meta:
        model = Autosalon
        fields = ('name', 'contact')

class AutoImageForm(forms.ModelForm):
    class Meta:
        model = AutoImage
        fields = ('image',)

class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ('reason',)

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['image']

class AutoImageForm(forms.ModelForm):
    class Meta:
        model = AutoImage
        fields = ['auto', 'image']
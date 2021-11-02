from django import forms
from .models import Beer

class BeerForm(forms.ModelForm):
    class Meta:
        model = Beer
        fields = ['text']
        labels = {'text':''}
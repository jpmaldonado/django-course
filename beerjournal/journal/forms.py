from django import forms
from .models import Beer, Entry

class BeerForm(forms.ModelForm):
    class Meta:
        model = Beer
        fields = ['text']
        labels = {'text':''}

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry        
        fields = ['text']
        labels = {'text':'Entry:'}
        widgets = {'text':forms.Textarea(attrs={'cols':80})}

        
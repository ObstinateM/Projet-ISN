from django import forms
from . import models

class CreateCard(forms.ModelForm):
    class Meta:
        model = models.Cartes
        fields = ['title','content']
        labels = {
            'title': 'Titre',
            'content': 'Contenu',
        }

class TranslateForm(forms.Form):
    wordEn = forms.CharField(label='Le mot en anglais :', max_length=100)
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
    
class ReviewCard(forms.Form):
    pass
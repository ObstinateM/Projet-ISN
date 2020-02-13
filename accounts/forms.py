from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    """A form that create a user with no privileges.
    """
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'placeholder':'exemple@flashcard.com'}))


    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        labels = {
            'username': 'Pseudo',
            'email' : "E-Mail",
            'password1' : 'Mot de passe'
        }
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': '150 caractères maximum.'}),
        }


    def __init__(self, *args, **kwargs):
            super(RegisterForm, self).__init__(*args, **kwargs)
            self.fields['password1'].widget = forms.PasswordInput(attrs={'placeholder':'Minimum 8 caractères.'})
            self.fields['password2'].widget = forms.PasswordInput(attrs={'placeholder':'Répéter votre mot de passe.'})

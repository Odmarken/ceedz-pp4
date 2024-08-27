# forms.py

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')  # Exclude 'email' here

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Remove unwanted fields if they exist
        if 'password_based_authentication' in self.fields:
            del self.fields['password_based_authentication']
        if 'email' in self.fields:
            del self.fields['email']

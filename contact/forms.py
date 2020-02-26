from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from accounts.models import Profile

class ContactForm(forms.Form):
        username = forms.CharField(required=True)
        email = forms.EmailField(required=True)
        message = forms.CharField(widget=forms.Textarea)

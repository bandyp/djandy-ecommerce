from django import forms

class ContactForm(forms.Form):
        name = forms.CharField(required=True, initial="class")
        email = forms.EmailField(required=True)
        message = forms.CharField(widget=forms.Textarea)

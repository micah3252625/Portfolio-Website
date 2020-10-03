from django import forms
from .models import Contacts

class NewContactForm(forms.ModelForm):
    class Meta:
        model = Contacts
        fields = ("name", "email", "subject", "message")
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'subject': forms.TextInput(attrs={'class': 'form-control'}),
            'message': forms.Textarea(attrs={'class': 'form-control'}),
        }

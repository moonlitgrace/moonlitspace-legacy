from django import forms

from .models import NewsLetterEntry

class NewsLetterEntryFrom(forms.ModelForm):
    class Meta:
        model = NewsLetterEntry
        fields = ("email", )

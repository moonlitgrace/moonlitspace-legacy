from django import forms

from .models import NewsLetterEntry


class NewsLetterEntryFrom(forms.ModelForm):
    class Meta:
        model = NewsLetterEntry
        fields = ("email",)
        widgets = {
            "email": forms.EmailInput(
                attrs={
                    "placeholder": "Email Address*",
                    "disabled": True,
                }
            )
        }

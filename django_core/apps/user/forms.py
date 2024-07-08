from django import forms
from django.core.exceptions import ValidationError

from .models import Profile

class ProfileAdminForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = "__all__"

    def clean(self):
        cleaned_data = super().clean()
        active = cleaned_data.get("active")
        type = cleaned_data.get("type")

        if active:
            if Profile.objects.filter(type=type, active=True).exclude(pk=self.instance.pk).exists():
                raise ValidationError(
                    {"type": "An active profile with the same type already exists."}
                )
        return cleaned_data

from django import forms
from projectapp.models.crm import Ishchi


class IshchiForm(forms.ModelForm):
    class Meta:
        model = Ishchi
        fields = "__all__"
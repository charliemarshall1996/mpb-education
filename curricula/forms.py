
from django import forms

from . import models


class TermForm(forms.ModelForm):
    start_date = forms.DateField(
        widget=forms.DateInput(attrs={"type": "date"}))
    end_date = forms.DateField(widget=forms.DateInput(attrs={"type": "date"}))

    class Meta:
        model = models.Term
        fields = ['subject', 'start_date', 'end_date']

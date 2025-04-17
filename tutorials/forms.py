from django import forms

from students import models as smodels
from . import models


class GroupForm(forms.ModelForm):
    students = forms.ModelMultipleChoiceField(
        queryset=smodels.Student.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )
    is_active = forms.BooleanField(widget=forms.CheckboxInput)

    class Meta:
        model = models.Group
        fields = [
            "term",
            "students",
            "is_active"
        ]

    def clean_students(self):
        students = self.cleaned_data.get("students")
        if students.count() > 6:
            raise forms.ValidationError(
                "You can only select up to 6 students.")
        return students


class TutorialForm(forms.ModelForm):
    date = forms.DateField(
        widget=forms.DateInput(attrs={"type": "date"}))
    start_time = forms.TimeField(
        widget=forms.TimeInput(attrs={"type": "time"})
    )
    end_time = forms.TimeField(
        widget=forms.TimeInput(attrs={"type": "time"})
    )

    class Meta:
        model = models.Tutorial
        fields = [
            "title",
            "meeting_link",
            "note",
            "date",
            "start_time",
            "end_time"
        ]

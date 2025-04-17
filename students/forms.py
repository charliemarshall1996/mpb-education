from django import forms

from . import models


class StudentForm(forms.ModelForm):
    date_of_birth = forms.DateField(
        widget=forms.DateInput(attrs={"type": "date"}))

    class Meta:
        model = models.Student
        fields = [
            "first_name",
            "last_name",
            "email",
            "date_of_birth",
            "notes",
            "guardian"
        ]


class TestimonialForm(forms.ModelForm):
    date = forms.DateField(
        widget=forms.DateInput(attrs={"type": "date"})
    )

    class Meta:
        model = models.Testimonial
        fields = [
            "guardian",
            "quote",
            "date"
        ]

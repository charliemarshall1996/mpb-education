"""Data models for the curricula app.

The curricula of MPB Education includes these models:
- Subject, pertaining to the different subjects taught.

"""
from django.db import models

# Create your models here.


class Subject(models.Model):
    """Model representation of subjects taught."""
    name = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):  # noqa: D105
        return self.name


class Term(models.Model):
    """Model representation of a subjects term."""
    subject = models.ForeignKey(
        Subject, on_delete=models.CASCADE, related_name='terms')
    start_date = models.DateField()
    end_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):  # noqa: D105
        return f"{self.subject.name} | {self.start_date} - {self.end_date}"

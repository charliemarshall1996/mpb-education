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

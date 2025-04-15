
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic

from . import models


class SubjectListView(generic.ListView, LoginRequiredMixin):
    model = models.Subject
    paginate_by = 10
    ordering = ["-name"]


from django import urls
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic

from . import models, forms


class SubjectListView(generic.ListView, LoginRequiredMixin):
    model = models.Subject
    paginate_by = 10
    ordering = ["-name"]


class SubjectDetailView(generic.DetailView, LoginRequiredMixin):
    model = models.Subject

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class SubjectCreateView(generic.CreateView, LoginRequiredMixin):
    model = models.Subject
    fields = [
        "name"
    ]
    success_url = urls.reverse_lazy("curricula:subject-list")


class SubjectUpdateView(generic.UpdateView, LoginRequiredMixin):
    model = models.Subject
    fields = [
        "name"
    ]

    def get_success_url(self):
        # Redirect to the detail view of the updated Subject
        return urls.reverse("curricula:subject-detail", kwargs={"pk": self.object.pk})


class SubjectDeleteView(generic.DeleteView, LoginRequiredMixin):
    model = models.Subject
    success_url = urls.reverse_lazy("curricula:subject-list")


class TermListView(generic.ListView, LoginRequiredMixin):
    model = models.Term
    paginate_by = 10
    ordering = ["-start_date"]


class TermDetailView(generic.DetailView, LoginRequiredMixin):
    model = models.Term

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class TermCreateView(generic.CreateView, LoginRequiredMixin):
    model = models.Term
    form_class = forms.TermForm
    success_url = urls.reverse_lazy("curricula:term-list")


class TermUpdateView(generic.UpdateView, LoginRequiredMixin):
    model = models.Term
    form_class = forms.TermForm

    def get_success_url(self):
        # Redirect to the detail view of the updated Subject
        return urls.reverse("curricula:term-detail", kwargs={"pk": self.object.pk})


class TermDeleteView(generic.DeleteView, LoginRequiredMixin):
    model = models.Term
    success_url = urls.reverse_lazy("curricula:term-list")

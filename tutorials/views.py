from . import models, forms
from django import urls
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic

from . import models


class GroupListView(generic.ListView, LoginRequiredMixin):
    model = models.Group
    paginate_by = 10


class GroupDetailView(generic.DetailView, LoginRequiredMixin):
    model = models.Group

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class GroupCreateView(generic.CreateView, LoginRequiredMixin):
    model = models.Group
    form_class = forms.GroupForm
    success_url = urls.reverse_lazy("tutorials:group-list")


class GroupUpdateView(generic.UpdateView, LoginRequiredMixin):
    model = models.Group
    form_class = forms.GroupForm

    def get_success_url(self):
        # Redirect to the detail view of the updated Group
        return urls.reverse("tutorials:group-detail", kwargs={"pk": self.object.pk})


class GroupDeleteView(generic.DeleteView, LoginRequiredMixin):
    model = models.Group
    success_url = urls.reverse_lazy("tutorials:group-list")


class TutorialListView(generic.ListView, LoginRequiredMixin):
    model = models.Tutorial
    paginate_by = 10
    ordering = ["-date", "-start_time"]


class TutorialDetailView(generic.DetailView, LoginRequiredMixin):
    model = models.Tutorial

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class TutorialCreateView(generic.CreateView, LoginRequiredMixin):
    model = models.Tutorial
    form_class = forms.TutorialForm
    success_url = urls.reverse_lazy("tutorials:tutorial-list")


class TutorialUpdateView(generic.UpdateView, LoginRequiredMixin):
    model = models.Tutorial
    form_class = forms.TutorialForm

    def get_success_url(self):
        # Redirect to the detail view of the updated Tutorial
        return urls.reverse("tutorials:tutorial-detail", kwargs={"pk": self.object.pk})


class TutorialDeleteView(generic.DeleteView, LoginRequiredMixin):
    model = models.Tutorial
    success_url = urls.reverse_lazy("tutorials:tutorial-list")

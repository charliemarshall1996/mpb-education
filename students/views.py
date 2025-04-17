from django import urls
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic

from . import models, forms


class GuardianListView(generic.ListView, LoginRequiredMixin):
    model = models.Guardian
    paginate_by = 10
    ordering = ["-first_name", "-last_name"]


class GuardianDetailView(generic.DetailView, LoginRequiredMixin):
    model = models.Guardian

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class GuardianCreateView(generic.CreateView, LoginRequiredMixin):
    model = models.Guardian
    fields = [
        "first_name",
        "last_name",
        "email",
        "phone",
        "address_line_1",
        "address_line_2",
        "city",
        "county"
    ]
    success_url = urls.reverse_lazy("students:guardian-list")


class GuardianUpdateView(generic.UpdateView, LoginRequiredMixin):
    model = models.Guardian
    fields = [
        "first_name",
        "last_name",
        "email",
        "phone",
        "address_line_1",
        "address_line_2",
        "city",
        "county"
    ]

    def get_success_url(self):
        # Redirect to the detail view of the updated Guardian
        return urls.reverse("students:guardian-detail", kwargs={"pk": self.object.pk})


class GuardianDeleteView(generic.DeleteView, LoginRequiredMixin):
    model = models.Guardian
    success_url = urls.reverse_lazy("students:guardian-list")


class StudentListView(generic.ListView, LoginRequiredMixin):
    model = models.Student
    paginate_by = 10
    ordering = ["-first_name", "-last_name"]


class StudentDetailView(generic.DetailView, LoginRequiredMixin):
    model = models.Student

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class StudentCreateView(generic.CreateView, LoginRequiredMixin):
    model = models.Student
    form_class = forms.StudentForm
    success_url = urls.reverse_lazy("students:student-list")


class StudentUpdateView(generic.UpdateView, LoginRequiredMixin):
    model = models.Student
    form_class = forms.StudentForm

    def get_success_url(self):
        # Redirect to the detail view of the updated Subject
        return urls.reverse("students:student-detail", kwargs={"pk": self.object.pk})


class StudentDeleteView(generic.DeleteView, LoginRequiredMixin):
    model = models.Student
    success_url = urls.reverse_lazy("students:student-list")

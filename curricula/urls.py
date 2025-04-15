from django.urls import path

from . import views

app_name = "curricula"

urlpatterns = [
    path("subjects", views.SubjectListView.as_view(),
         name="subject-list"),
    path("subject/<int:pk>", views.SubjectDetailView.as_view(),
         name="subject-detail"),
    path(
        "subject/update/<int:pk>",
        views.SubjectUpdateView.as_view(),
        name="subject-update",
    ),
    path("subject/create", views.SubjectCreateView.as_view(),
         name="subject-create"),
    path("subject/delete/<int:pk>",
         views.SubjectDeleteView.as_view(), name="subject-delete")
]

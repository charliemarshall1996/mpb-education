from django.urls import path

from . import views

app_name = "curricula"

urlpatterns = [

    # Subject views
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
         views.SubjectDeleteView.as_view(), name="subject-delete"),

    # Term Views
    path("terms", views.TermListView.as_view(),
         name="term-list"),
    path("term/<int:pk>", views.TermDetailView.as_view(),
         name="term-detail"),
    path(
        "term/update/<int:pk>",
        views.TermUpdateView.as_view(),
        name="term-update",
    ),
    path("term/create", views.TermCreateView.as_view(),
         name="term-create"),
    path("term/delete/<int:pk>",
         views.TermDeleteView.as_view(), name="term-delete")
]

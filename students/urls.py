from django.urls import path

from . import views

app_name = "students"

urlpatterns = [

    # Guardian views
    path("guardians", views.GuardianListView.as_view(),
         name="guardian-list"),
    path("guardian/<int:pk>", views.GuardianDetailView.as_view(),
         name="guardian-detail"),
    path(
        "guardian/update/<int:pk>",
        views.GuardianUpdateView.as_view(),
        name="guardian-update",
    ),
    path("guardian/create", views.GuardianCreateView.as_view(),
         name="guardian-create"),
    path("guardian/delete/<int:pk>",
         views.GuardianDeleteView.as_view(), name="guardian-delete"),

    # Student Views
    path("students", views.StudentListView.as_view(),
         name="student-list"),
    path("student/<int:pk>", views.StudentDetailView.as_view(),
         name="student-detail"),
    path(
        "student/update/<int:pk>",
        views.StudentUpdateView.as_view(),
        name="student-update",
    ),
    path("student/create", views.StudentCreateView.as_view(),
         name="student-create"),
    path("student/delete/<int:pk>",
         views.StudentDeleteView.as_view(), name="student-delete")
]

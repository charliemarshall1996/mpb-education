from django.urls import path

from . import views

app_name = "tutorials"

urlpatterns = [
    # Guardian views
    path("tutorials", views.TutorialListView.as_view(),
         name="tutorial-list"),
    path("tutorial/<int:pk>", views.TutorialDetailView.as_view(),
         name="tutorial-detail"),
    path(
        "tutorial/update/<int:pk>",
        views.TutorialUpdateView.as_view(),
        name="tutorial-update",
    ),
    path("tutorial/create", views.TutorialCreateView.as_view(),
         name="tutorial-create"),
    path("tutorial/delete/<int:pk>",
         views.TutorialDeleteView.as_view(), name="tutorial-delete"),

    # Student Views
    path("groups", views.GroupListView.as_view(),
         name="group-list"),
    path("group/<int:pk>", views.GroupDetailView.as_view(),
         name="group-detail"),
    path(
        "group/update/<int:pk>",
        views.GroupUpdateView.as_view(),
        name="group-update",
    ),
    path("group/create", views.GroupCreateView.as_view(),
         name="group-create"),
    path("group/delete/<int:pk>",
         views.GroupDeleteView.as_view(), name="group-delete"),
]

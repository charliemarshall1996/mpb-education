from django.urls import path

from . import views

app_name = "mpbadmin"

urlpatterns = [
    path("login/", views.AdminLoginView.as_view(), name="login")
]

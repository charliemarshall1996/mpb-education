from django.contrib.auth.views import LoginView


class AdminLoginView(LoginView):
    template_name = "mpbadmin/login.html"
    next_page = "curricula:subject-list"  # Use the URL name as a string

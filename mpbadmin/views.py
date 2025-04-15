
from django.contrib.auth.views import LoginView
# Create your views here.


class AdminLoginView(LoginView):
    template_name = "mpbadmin/login.html"

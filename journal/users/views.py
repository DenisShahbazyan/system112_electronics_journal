from django.contrib.auth.views import LoginView

from .forms import UserAuthenticationForm


class UserLoginView(LoginView):
    form_class = UserAuthenticationForm
    template_name = 'users/login.html'

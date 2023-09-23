from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm

User = get_user_model()


class UserAuthenticationForm(AuthenticationForm):
    """Форма авторизации."""
    class Meta(AuthenticationForm):
        model = User
        fields = ('email', 'password')

from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm
from django import forms

User = get_user_model()


class UserAuthenticationForm(AuthenticationForm):
    """Форма авторизации."""
    username = forms.EmailField()

    class Meta(AuthenticationForm):
        model = User
        fields = ('username', 'password')

    def clean_username(self):
        username = self.cleaned_data['username'].lower()
        return username

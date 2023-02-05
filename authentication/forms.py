from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django import forms


class SignUpForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ["username"]


class LoginForm(forms.Form):
    username = forms.CharField(max_length=64, label="Username")
    password = forms.CharField(
        max_length=64, widget=forms.PasswordInput, label="Password"
    )

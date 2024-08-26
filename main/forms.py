from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from users.models import CustomUser


class RegisterUserForm(UserCreationForm):
    first_name = forms.CharField(max_length=50, required=True, widget=forms.TextInput())
    last_name = forms.CharField(max_length=50, required=True, widget=forms.TextInput())
    username = forms.CharField(max_length=20, required=True, widget=forms.TextInput())
    email = forms.EmailField(required=True, widget=forms.EmailInput())
    password1 = forms.CharField(required=True, widget=forms.PasswordInput())
    password2 = forms.CharField(required=True, widget=forms.PasswordInput())

    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(max_length=50, required=True, widget=forms.TextInput())
    password = forms.CharField(required=True, widget=forms.PasswordInput())

    class Meta:
        model = CustomUser
        fields = ('username', 'password')

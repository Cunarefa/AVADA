import re

from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from movie_app.models import User


class UserRegisterForm(UserCreationForm):
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={"class": 'form-control'}))
    password2 = forms.CharField(label='Подтверждение пароля',
                                widget=forms.PasswordInput(attrs={"class": 'form-control'}))

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2']


class UserLoginForm(AuthenticationForm):
    username = forms.EmailField(label='E-mail', widget=forms.EmailInput())
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput())




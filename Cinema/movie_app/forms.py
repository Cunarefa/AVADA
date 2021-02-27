from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User

from movie_app.models import Movie


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput())
    email = forms.EmailField(label='Email', widget=forms.EmailInput())
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput())
    password2 = forms.CharField(label='Подтвердите пароль', widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={"placeholder": "Username"}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={"placeholder": "Password"}))


# Тестовые +++++++++++++++++++++++++++++++++++++++++++++++++++

class CreateMovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        # fields = [
        #     'title', 'description', 'poster', 'genre', 'premier',
        #     'on_screen', 'year', 'country', 'actors', 'age'
        # ]
        exclude = ['slug']


class AdminCreateMovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        # fields = '__all__'
        exclude = ['slug']
        widgets = {
            'title': forms.TextInput(),
            'slug': forms.TextInput(),
            'description': forms.Textarea(attrs={'rows': 5}),
            'poster': forms.FileInput(),
            'genre': forms.Select(),
            'premier': forms.DateInput(),
            'on_screen': forms.CheckboxInput(),
            'year': forms.NumberInput(),
            'country': forms.TextInput(),
            'actors': forms.TextInput(),
            'age': forms.TextInput(),
        }


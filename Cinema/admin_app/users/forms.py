from django import forms
from django.contrib.auth.forms import PasswordChangeForm

from movie_app.models import User


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'first_name', 'last_name', 'email', 'address', 'password', 'card_number',
            'language', 'gender', 'date_of_birth', 'city'
        ]
        widgets = {
            'address': forms.TextInput(),
            'language': forms.RadioSelect(),
            'gender': forms.RadioSelect(),
            'date_of_birth': forms.DateInput(attrs={'id': 'datepicker'})
        }


class ChangePassword(PasswordChangeForm):
    old_password = forms.CharField(required=True, label='Старый пароль',
                                   widget=forms.PasswordInput(attrs={
                                       'class': 'form-control'}))
    new_password1 = forms.CharField(required=True, label='Новый пароль',
                                    widget=forms.PasswordInput(attrs={
                                        'class': 'form-control'}))
    new_password2 = forms.CharField(required=True, label='Повторите пароль',
                                    widget=forms.PasswordInput(attrs={
                                        'class': 'form-control'}),
                                    error_messages={
                                        'required': 'Пароль должны совпадать!'})

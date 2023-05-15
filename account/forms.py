from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from account.models import User


class UserLoginForm(AuthenticationForm):
    username = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form-control forma-vxoda', 'placeholder': 'Введите адрес эл. почты'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control forma-vxoda', 'placeholder': 'Введите пароль'
    }))

    class Meta:
        model = User
        fields = ('username', 'password')


class UserRegistrationForm(UserCreationForm):
    username = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form-control forma-vxoda', 'placeholder': 'Введите адрес эл. почты'
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control forma-vxoda', 'placeholder': 'Введите пароль'
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control forma-vxoda', 'placeholder': 'Подтвердите пароль'
    }))

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')

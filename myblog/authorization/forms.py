from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from .models import Auth
from django import forms

class authForm(forms.ModelForm):
    class Meta:
        model = Auth
        fields = ['login', 'password']
        widgets = {
            "login": forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'логин'
            }),
            "password": forms.PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'пароль'
            })
        }
class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget = forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))



class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        # widgets = {
        #     'username': forms.TextInput(attrs={
        #         'class': 'form-control'
        #     }),
        #     "password1": forms.PasswordInput(attrs={
        #         'class': 'form-control',
        #     }),
        #     "password2": forms.PasswordInput(attrs={
        #         'class': 'form-control'
        #     })
        # }
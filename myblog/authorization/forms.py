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
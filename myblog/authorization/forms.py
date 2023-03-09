from .models import Auth
from django import forms

class authForm(forms.ModelForm):
    class Meta:
        model = Auth
        fields = ['login', 'password']
        widgets = {
            "title": forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'логин'
            }),
            "anons": forms.PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'пароль'
            })
        }
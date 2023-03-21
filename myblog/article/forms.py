from .models import article
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea, SelectDateWidget, SplitDateTimeWidget, \
    DateTimeField


class articleForm(ModelForm):
    class Meta:
        model = article
        fields = ['title', 'anons', 'content', 'date']
        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'название статьи'
            }),
            "anons": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'анонс'
            }),
            "content": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'содержание'
            }),
            "date": DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата и время: dd-mm-YYYY hh:mm:ss'
            })
        }
from django.db import models


class Auth(models.Model):
    login = models.SlugField(max_length=20, unique=True)
    password = models.SlugField(max_length=16)

    def __str__(self):
        return self.login

    class Meta:
         verbose_name = 'Данные'
         verbose_name_plural = 'Данные'


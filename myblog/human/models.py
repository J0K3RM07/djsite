from django.db import models

class students(models.Model):
    id = models.CharField(max_length=30, primary_key=True)
    name = models.CharField(max_length=15)
    surname = models.CharField(max_length=15)
    patronymic = models.CharField(max_length=15)
    content = models.TextField()
    group = models.SlugField(allow_unicode=True)
    telephone = models.IntegerField(unique=True)









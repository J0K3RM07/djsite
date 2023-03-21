from django.db import models
from django.shortcuts import reverse
from time import gmtime, strftime

class article(models.Model):
    title = models.CharField('Название',max_length=50)
    anons = models.CharField('Анонс',max_length=150)
    content = models.TextField('Содержимое')
    date = models.DateTimeField('Дата публикации', default=strftime("%Y-%m-%d %H:%M:%S", gmtime()), blank=True)
    cat = models.ForeignKey('category', on_delete=models.PROTECT, null=True)


    def get_absolute_url(self):
        return reverse('auth')

    def __str__(self):
        return self.title



    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

class category(models.Model):
    TypeOfAudience = models.CharField(max_length=20, db_index=True)

    def __str__(self):
        return self.TypeOfAudience
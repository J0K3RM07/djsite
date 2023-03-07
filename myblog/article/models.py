from django.db import models

class article(models.Model):
    title = models.CharField('Название',max_length=50)
    anons = models.CharField('Анонс',max_length=150)
    content = models.TextField('Содержимое')
    date = models.DateTimeField('Дата публикации')



    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'


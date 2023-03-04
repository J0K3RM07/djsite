from django.db import models

class article(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    date = models.DateField()



    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'








from django.db import models

class MainMenu(models.Model):
    name = models.CharField(max_length=50)
    url_slug = models.SlugField(unique=True, db_index=True, verbose_name="Url")
    class Meta:
        verbose_name = 'Главное меню'
        verbose_name_plural = 'Главное меню'

    def __str__(self):
        return self.name

class SubMenu(models.Model):
    main_cat = models.ForeignKey(MainMenu, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    url_slug = models.SlugField(unique=True, db_index=True, verbose_name="Url")

    class Meta:
        verbose_name = 'Подменю'
        verbose_name_plural = 'Подменю'

    def __str__(self):
        return self.name

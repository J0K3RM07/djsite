# Generated by Django 4.1.7 on 2023-03-20 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0003_alter_article_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='date',
            field=models.DateTimeField(blank=True, default='2023-03-20 17:16:58', verbose_name='Дата публикации'),
        ),
    ]
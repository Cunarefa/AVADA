# Generated by Django 3.1.6 on 2021-02-21 13:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0005_auto_20210221_1205'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='on_screen',
            field=models.BooleanField(default=True, verbose_name='В прокате'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='premier',
            field=models.DateField(default=datetime.date(2021, 2, 21), verbose_name='Дата премьеры'),
        ),
    ]

from datetime import date

from django.db import models
from django.urls import reverse
from multiselectfield import MultiSelectField

from embed_video.fields import EmbedVideoField


class Movie(models.Model):
    TYPES_OF_SCREEN = (
        ('3D', '3D'),
        ('2D', '2D'),
        ('IMAX', 'IMAX'),
    )

    title = models.CharField(max_length=100, verbose_name='Название')
    slug = models.SlugField(unique=True)
    description = models.TextField(verbose_name='Описание')
    poster = models.ImageField(upload_to='posters/%Y/%m/%d/', verbose_name='Постер')
    genre = models.ManyToManyField('Genre', verbose_name='Жанр', related_name='related_genres')
    trailer = EmbedVideoField(blank=True, verbose_name='Трейлер', null=True)
    screen_types = MultiSelectField(verbose_name='Типы кино', choices=TYPES_OF_SCREEN)
    premier = models.DateField(default=date.today, verbose_name='Дата премьеры')
    on_screen = models.BooleanField(default=True, verbose_name='В прокате')
    year = models.PositiveIntegerField(default=2021, verbose_name='Год выпуска')
    country = models.CharField(max_length=100, default='USA', verbose_name='Страна')
    actors = models.CharField(max_length=1000, verbose_name='Актеры', blank=True)
    age = models.CharField(max_length=3, verbose_name='Возраст', default='6+')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('movie_detail', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'


class Gallery(models.Model):
    image = models.ImageField(upload_to='gallery', blank=True)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='movie_images')
    cinema = models.ForeignKey('Cinema', on_delete=models.CASCADE, related_name='cinema_images')

    class Meta:
        verbose_name = 'Галерея'


class Genre(models.Model):
    name = models.CharField(max_length=25, verbose_name='Название')
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'


class Cinema(models.Model):
    name = models.CharField(max_length=55, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    conditions = models.TextField(verbose_name='Условия', blank=True)
    logo = models.ImageField(upload_to='cinema_logos', verbose_name='Логотип')
    # hall = models.ForeignKey()













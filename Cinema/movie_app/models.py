from datetime import date

from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
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
    slug = models.SlugField(unique=True, verbose_name='URL')
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


class Cinema(models.Model):
    name = models.CharField(max_length=55, verbose_name='Название')
    slug = models.SlugField(unique=True, verbose_name='URL')
    description = models.TextField(verbose_name='Описание')
    top_banner = models.ImageField(upload_to='cinema_banners', verbose_name='Фото')
    conditions = models.TextField(verbose_name='Условия', blank=True)
    logo = models.ImageField(upload_to='cinema_logos', verbose_name='Логотип', blank=True, null=True)

    class Meta:
        verbose_name = 'Кинотеатр'
        verbose_name_plural = 'Кинотеатры'


class Hall(models.Model):
    name = models.CharField(max_length=30, verbose_name='Название')
    slug = models.SlugField(unique=True)
    description = models.TextField(verbose_name='Описание')
    top_banner = models.ImageField(upload_to='hall_banners', verbose_name='Фото')
    scheme = models.ImageField(upload_to='hall_scheme', verbose_name='Схема')
    cinema = models.ForeignKey(Cinema, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Зал'
        verbose_name_plural = 'Залы'


class Gallery(models.Model):
    image = models.ImageField(upload_to='gallery', blank=True, null=True)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()

    class Meta:
        verbose_name = 'Галерея'
        verbose_name_plural = 'Галереи'


class Genre(models.Model):
    name = models.CharField(max_length=25, verbose_name='Название')
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'




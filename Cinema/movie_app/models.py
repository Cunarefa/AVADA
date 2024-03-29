from datetime import date

from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.urls import reverse
from multiselectfield import MultiSelectField
from embed_video.fields import EmbedVideoField
from pytils.translit import slugify


class Gallery(models.Model):
    image = models.ImageField(upload_to='gallery', blank=True, null=True)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()

    class Meta:
        verbose_name = 'Галерея'
        verbose_name_plural = 'Галереи'


class Movie(models.Model):
    TYPES_OF_SCREEN = (
        ('3D', '3D'),
        ('2D', '2D'),
        ('IMAX', 'IMAX'),
    )

    title = models.CharField(max_length=100, verbose_name='Название')
    slug = models.SlugField(unique=True, verbose_name='URL')
    description = RichTextUploadingField(verbose_name='Описание', blank=True)
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

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('movie_detail', kwargs={'slug': self.slug})


class MovieGallery(models.Model):
    image = models.ImageField(upload_to='movie_gallery', verbose_name='Фото', blank=True, null=True)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)


class Cinema(models.Model):
    name = models.CharField(max_length=55, verbose_name='Название')
    slug = models.SlugField(unique=True, verbose_name='URL')
    description = RichTextUploadingField(verbose_name='Описание', blank=True)
    conditions = models.TextField(verbose_name='Условия', blank=True)
    logo = models.ImageField(upload_to='cinema_logos', verbose_name='Логотип', blank=True, null=True)
    top_banner = models.ImageField(upload_to='cinema_banners', verbose_name='Верхний баннер')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('cinema_item', kwargs={'slug': self.slug})


class CinemaGallery(models.Model):
    image = models.ImageField(upload_to='cinema_gallery', verbose_name='Фото', blank=True, null=True)
    cinema = models.ForeignKey(Cinema, on_delete=models.CASCADE)


class Hall(models.Model):
    name = models.CharField(max_length=30, verbose_name='Название')
    description = RichTextUploadingField(verbose_name='Описание', blank=True)
    top_banner = models.ImageField(upload_to='hall_banners', verbose_name='Верхний баннер', blank=True)
    scheme = models.ImageField(upload_to='hall_scheme', verbose_name='Схема', blank=True)
    cinema = models.ForeignKey(Cinema, on_delete=models.CASCADE, verbose_name='Кинотеатр', related_name='cinema_halls')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('hall_item', kwargs={'pk': self.pk})


class HallGallery(models.Model):
    image = models.ImageField(upload_to='hall_gallery', verbose_name='Фото', blank=True, null=True)
    hall = models.ForeignKey(Hall, on_delete=models.CASCADE, related_name='halls_photo')


class Genre(models.Model):
    name = models.CharField(max_length=25, verbose_name='Название')
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Pages(models.Model):
    title = models.CharField(max_length=55, verbose_name='Название')
    description = RichTextUploadingField(verbose_name='Описание', blank=True)
    main_photo = models.ImageField(upload_to='pages_photo', verbose_name='Главное фото', blank=True)
    created_at = models.DateField(auto_now_add=True, verbose_name='Дата создания')

    class Meta:
        abstract = True

    def __str__(self):
        return self.title


class News(Pages):
    pass


class NewsGallery(models.Model):
    image = models.ImageField(upload_to='news_gallery', verbose_name='Фото', blank=True, null=True)
    news = models.ForeignKey(News, on_delete=models.CASCADE)


class Action(Pages):
    def get_absolute_url(self):
        return reverse('action_item', kwargs={'pk': self.pk})


class ActionGallery(models.Model):
    image = models.ImageField(upload_to='action_gallery', verbose_name='Фото', blank=True, null=True)
    news = models.ForeignKey(Action, on_delete=models.CASCADE)


class Cafe(Pages):
    def get_absolute_url(self):
        pass


class CafeGallery(models.Model):
    image = models.ImageField(upload_to='cafe_gallery', verbose_name='Фото', blank=True, null=True)
    news = models.ForeignKey(Cafe, on_delete=models.CASCADE)


class VIPHall(Pages):
    def get_absolute_url(self):
        pass


class VIPHallGallery(models.Model):
    image = models.ImageField(upload_to='vipHall_gallery', verbose_name='Фото', blank=True, null=True)
    news = models.ForeignKey(VIPHall, on_delete=models.CASCADE)


class ChildrenRoom(Pages):
    def get_absolute_url(self):
        pass


class ChildrenRoomGallery(models.Model):
    image = models.ImageField(upload_to='childRoom_gallery', verbose_name='Фото', blank=True, null=True)
    news = models.ForeignKey(ChildrenRoom, on_delete=models.CASCADE)


class Advertise(Pages):
    def get_absolute_url(self):
        pass


class AdvertiseGallery(models.Model):
    image = models.ImageField(upload_to='advertise_gallery', verbose_name='Фото', blank=True, null=True)
    news = models.ForeignKey(Advertise, on_delete=models.CASCADE)


class Contacts(models.Model):
    cinema_name = models.CharField(max_length=55, verbose_name='Название кинотеатра')
    address = models.CharField(max_length=155, verbose_name='Адрес')
    map_cords = RichTextUploadingField(verbose_name='Ссылка на карту')
    cinema = models.ForeignKey(Cinema, on_delete=models.CASCADE, verbose_name='Кинотеатр', related_name='cinema_contacts')

from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline
from django.utils.safestring import mark_safe

from .models import Gallery, Movie, Genre, Cinema, Hall


class GalleryInline(GenericTabularInline):
    model = Gallery


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    inlines = [GalleryInline]
    prepopulated_fields = {"slug": ("title",)}
    list_display = ['title', 'on_screen', 'get_photo']
    search_fields = ('title',)
    list_filter = ('genre',)

    def get_photo(self, obj):
        if obj.poster:
            return mark_safe(f'<img src="{obj.poster.url}" width="60">')
        return '-'

    get_photo.short_description = 'Миниатюрка'

    class Meta:
        model = Movie
        fields = '__all__'


@admin.register(Cinema)
class CinemaAdmin(admin.ModelAdmin):
    inlines = [GalleryInline]
    prepopulated_fields = {"slug": ("name",)}
    list_display = ['name', 'get_photo']
    search_fields = ('name',)

    def get_photo(self, obj):
        if obj.top_banner:
            return mark_safe(f'<img src="{obj.top_banner.url}" width="60">')
        return '-'

    get_photo.short_description = 'Миниатюрка'

    class Meta:
        model = Cinema
        fields = '__all__'


@admin.register(Hall)
class HallAdmin(admin.ModelAdmin):
    inlines = [GalleryInline]
    list_display = ['name']
    search_fields = ('name',)

    class Meta:
        model = Hall
        fields = '__all__'


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

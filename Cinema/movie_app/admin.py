from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Gallery, Movie, Genre


class GalleryInline(admin.TabularInline):
    fk_name = 'movie'
    model = Gallery


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    inlines = [GalleryInline, ]
    prepopulated_fields = {"slug": ("title",)}
    list_display = ['title', 'on_screen', 'get_photo']
    search_fields = ('title',)
    list_filter = ('genre', )

    def get_photo(self, obj):
        if obj.poster:
            return mark_safe(f'<img src="{obj.poster.url}" width="60">')
        return '-'

    get_photo.short_description = 'Миниатюрка'

    class Meta:
        model = Movie
        fields = '__all__'


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

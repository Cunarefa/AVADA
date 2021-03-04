from django import forms
from django.contrib.contenttypes.models import ContentType
from django.forms.models import inlineformset_factory

from movie_app.models import Movie, Gallery, MovieGallery


class AdminCreateMovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        exclude = ['slug']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 5}),
        }


GalleryFormset = inlineformset_factory(ContentType, Gallery, fields=['image'], extra=4)

GalleryMovieFormset = inlineformset_factory(Movie, MovieGallery, fields=('image',), max_num=3)

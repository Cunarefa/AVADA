from django import forms
from django.forms.models import inlineformset_factory
from ckeditor.widgets import CKEditorWidget
from movie_app.models import Movie, MovieGallery


class AdminCreateMovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        exclude = ['slug']
        widgets = {
            'premier': forms.DateInput(attrs={'id': 'datepicker'}),
            'description': CKEditorWidget(),
        }


GalleryMovieFormset = inlineformset_factory(Movie, MovieGallery, fields=('image',), max_num=3)

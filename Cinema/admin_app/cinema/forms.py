from django import forms
from django.forms import inlineformset_factory
from ckeditor.widgets import CKEditorWidget
from movie_app.models import Cinema, CinemaGallery


class CinemaAdminForm(forms.ModelForm):
    class Meta:
        model = Cinema
        exclude = ['slug']
        widgets = {
            'description': CKEditorWidget(),
            'conditions': CKEditorWidget(),
        }


CinemaFormset = inlineformset_factory(Cinema, CinemaGallery, fields=('image',), max_num=3)

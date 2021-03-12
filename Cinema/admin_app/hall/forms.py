from ckeditor.widgets import CKEditorWidget
from django import forms
from django.forms import inlineformset_factory

from movie_app.models import Hall, HallGallery


class HallForm(forms.ModelForm):
    class Meta:
        model = Hall
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': CKEditorWidget(),
        }


HallGalleryFormset = inlineformset_factory(Hall, HallGallery, fields=('image',))

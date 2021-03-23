from ckeditor.widgets import CKEditorWidget
from django import forms
from django.forms import inlineformset_factory

from movie_app.models import News, NewsGallery


class NewsAdminForm(forms.ModelForm):
    class Meta:
        model = News
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': CKEditorWidget(),
        }

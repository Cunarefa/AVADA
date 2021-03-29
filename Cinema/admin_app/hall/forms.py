from ckeditor.widgets import CKEditorWidget
from django import forms

from movie_app.models import Hall


class HallForm(forms.ModelForm):
    class Meta:
        model = Hall
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': CKEditorWidget(),
        }

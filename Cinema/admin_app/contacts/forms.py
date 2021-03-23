from ckeditor.widgets import CKEditorWidget
from django import forms

from movie_app.models import Contacts


class ContactsForm(forms.ModelForm):
    class Meta:
        model = Contacts
        fields = '__all__'

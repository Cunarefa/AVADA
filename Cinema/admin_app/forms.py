from django import forms

from movie_app.models import Movie


class AdminCreateMovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        exclude = ['slug']
        widgets = {
            'title': forms.TextInput(),
            'slug': forms.TextInput(),
            'description': forms.Textarea(attrs={'rows': 5}),
            'poster': forms.FileInput(),
            'genre': forms.SelectMultiple(),
            'premier': forms.DateInput(),
            'on_screen': forms.CheckboxInput(),
            'year': forms.NumberInput(),
            'country': forms.TextInput(),
            'actors': forms.TextInput(),
            'age': forms.TextInput(),
        }

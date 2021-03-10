from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import UpdateView, DeleteView

from django.views.generic.base import View

from admin_app.movie.forms import AdminCreateMovieForm, GalleryMovieFormset
from movie_app.models import Movie


def admin_app(request):
    return render(request, 'base_admin.html')


class AdminAllMoviesList(View):
    def get(self, request, *args, **kwargs):
        movies = Movie.objects.filter(on_screen=True)
        unreleased = Movie.objects.filter(on_screen=False).order_by('premier')[:4]
        context = {
            'movies': movies,
            'unreleased': unreleased,
            'title': 'Список фильмов'
        }
        return render(request, 'admin_app/admin_movies_list.html', context=context)


def admin_create_movie(request):
    movie = Movie()
    if request.method == 'POST':
        form = AdminCreateMovieForm(request.POST, request.FILES, instance=movie)
        formset = GalleryMovieFormset(request.POST, request.FILES, instance=movie)
        if form.is_valid() and formset.is_valid():
            form.save()
            formset.save()
            return redirect('admin_movies')
    else:
        formset = GalleryMovieFormset()
        form = AdminCreateMovieForm()

    context = {
        'formset': formset,
        'form': form,
        'title': 'Добавиьт фильм'
    }
    return render(request, 'admin_app/admin_create_movie.html', context=context)


class AdminUpdateMovie(UpdateView):
    model = Movie
    form_class = AdminCreateMovieForm
    template_name = 'admin_app/admin_create_movie.html'

    def get_context_data(self, **kwargs):
        context = super(AdminUpdateMovie, self).get_context_data(**kwargs)
        context['title'] = 'Обновление фильма'
        if self.request.POST:
            context['form'] = AdminCreateMovieForm(self.request.POST, self.request.FILES, instance=self.object)
            context['formset'] = GalleryMovieFormset(self.request.POST, self.request.FILES, instance=self.object)
        else:
            context['form'] = AdminCreateMovieForm(instance=self.object)
            context['formset'] = GalleryMovieFormset(instance=self.object)
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = AdminCreateMovieForm(request.POST, request.FILES, instance=self.object)
        formset = GalleryMovieFormset(request.POST, request.FILES, instance=self.object)
        if form.is_valid() and formset.is_valid():
            return self.form_valid(request, form, formset)
        return self.form_invalid(form)

    def form_valid(self, request, form, formset):
        if 'Удалить' in self.request.POST:
            movie_delete = Movie.objects.get(slug=self.kwargs['slug'])
            movie_delete.delete()
        else:
            self.object = form.save()
            formset.instance = self.object
            formset.save()
        return HttpResponseRedirect(reverse_lazy('admin_movies'))


class AdminDeleteMovie(DeleteView):
    model = Movie
    success_url = reverse_lazy('admin_movies')
    template_name = 'admin_app/delete.html'

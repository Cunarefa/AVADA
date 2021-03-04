from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from django.views.generic.base import View

from admin_app.forms import AdminCreateMovieForm, GalleryFormset, GalleryMovieFormset
from movie_app.models import Cinema, Movie, Gallery


def admin_app(request):
    return render(request, 'base_admin.html')


class AdminAllMoviesList(View):
    def get(self, request, *args, **kwargs):
        movies = Movie.objects.filter(on_screen=True)
        unreleased = Movie.objects.filter(on_screen=False).order_by('premier')[:4]
        context = {
            'movies': movies,
            'unreleased': unreleased,
        }
        return render(request, 'admin_app/admin_movies_list.html', context=context)


def create_movie(request):
    movie = Movie()
    if request.method == 'POST':
        formset = GalleryMovieFormset(request.POST, request.FILES, instance=movie)
        form = AdminCreateMovieForm(request.POST, request.FILES, instance=movie)
        if form.is_valid() and formset.is_valid():
            form.save()
            formset.save()
            return redirect('admin_movies')
    else:
        formset = GalleryMovieFormset()
        form = AdminCreateMovieForm()
    return render(request, 'admin_app/admin_create_movie.html', {'formset': formset, 'form': form})


class AdminUpdateMovie(UpdateView):
    model = Movie
    form_class = AdminCreateMovieForm
    template_name = 'admin_app/admin_update_movie.html'

    def get_context_data(self, **kwargs):
        context = super(AdminUpdateMovie, self).get_context_data(**kwargs)
        if self.request.POST:
            context['form'] = AdminCreateMovieForm(self.request.POST, self.request.FILES, instance=self.object)
            context['formset'] = GalleryMovieFormset(self.request.POST, self.request.FILES, instance=self.object)
        else:
            context['form'] = AdminCreateMovieForm(instance=self.object)
            context['formset'] = GalleryMovieFormset(instance=self.object)
        return context

    def form_valid(self, request):
        form = AdminCreateMovieForm(self.request.POST, self.request.FILES, instance=self.object)
        formset = GalleryMovieFormset(self.request.POST, self.request.FILES, instance=self.object)
        if 'Удалить' in self.request.POST:
            movie_delete = Movie.objects.get(slug=self.kwargs['slug'])
            movie_delete.delete()
        else:
            self.object = form.save()
            formset.instance = self.object
            formset.save()
            self.object = request.save()
        return HttpResponseRedirect(reverse_lazy('admin_movies'))


class AdminDeleteMovie(DeleteView):
    model = Movie
    success_url = reverse_lazy('admin_movies')
    template_name = 'admin_app/delete.html'

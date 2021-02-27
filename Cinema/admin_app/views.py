from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from django.views.generic.base import View

from admin_app.forms import AdminCreateMovieForm
from movie_app.models import Cinema, Movie


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


class AdminCreateMovie(CreateView):
    model = Movie
    form_class = AdminCreateMovieForm
    template_name = 'admin_app/admin_create_movie.html'
    success_url = reverse_lazy('admin_movies')


class AdminUpdateMovie(UpdateView):
    model = Movie
    form_class = AdminCreateMovieForm
    template_name = 'admin_app/admin_update_movie.html'
    context_object_name = 'update_movie'

    def form_valid(self, request):
        if 'Удалить' in self.request.POST:
            movie_delete = Movie.objects.get(slug=self.kwargs['slug'])
            movie_delete.delete()
            return HttpResponseRedirect(reverse_lazy('admin_movies'))
        else:
            self.object = request.save()
            return HttpResponseRedirect(reverse_lazy('admin_movies'))


class AdminDeleteMovie(DeleteView):
    model = Movie
    success_url = reverse_lazy('admin_movies')


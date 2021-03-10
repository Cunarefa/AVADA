from django.contrib import messages
from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, View, DetailView, CreateView, UpdateView

from .forms import UserRegisterForm, UserLoginForm
from .models import Movie, Cinema


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Поздравляем, регистрация успешна!')
            return redirect('main')
        else:
            messages.error(request, 'Ошибка регистрации')
    else:
        form = UserRegisterForm()
    return render(request, 'movie_app/register.html', {'form': form})


def user_login(request):
    if request.method == "POST":
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('main')
    else:
        form = UserLoginForm()
    return render(request, 'movie_app/login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('login')


class AllMovies(View):
    def get(self, request, *args, **kwargs):
        movies = Movie.objects.filter(on_screen=True)
        unreleased = Movie.objects.filter(on_screen=False).order_by('premier')[:4]
        context = {
            'movies': movies,
            'unreleased': unreleased,
        }
        return render(request, 'movie_app/main_page.html', context=context)


class MovieView(DetailView):
    model = Movie
    template_name = 'movie_app/movie_detail.html'
    context_object_name = 'movie_item'


class AfishaView(ListView):
    model = Movie
    template_name = 'movie_app/afisha.html'
    context_object_name = 'afisha'


class CinemaListView(ListView):
    model = Cinema
    template_name = 'movie_app/cinema_list.html'
    context_object_name = 'cinema_list'


class CinemaDetail(DetailView):
    model = Cinema
    template_name = 'movie_app/cinema_detail.html'
    context_object_name = 'cinema_view'

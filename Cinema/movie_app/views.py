from django.contrib import messages
from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, View, DetailView

from .forms import UserRegisterForm, UserLoginForm
from .models import Movie, Cinema, Hall, News, Action, Contacts


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

    def get_context_data(self, **kwargs):
        ctx = super(MovieView, self).get_context_data(**kwargs)
        ctx['title'] = Movie.objects.get(slug=self.kwargs['slug'])
        return ctx


class AfishaView(ListView):
    model = Movie
    template_name = 'movie_app/afisha.html'
    context_object_name = 'afisha'
    extra_context = {'title': 'Афиша'}


class CinemaListView(ListView):
    model = Cinema
    template_name = 'movie_app/cinema_list.html'
    context_object_name = 'cinema_list'
    extra_context = {'title': 'Кинотеатры'}


class CinemaDetail(DetailView):
    model = Cinema
    template_name = 'movie_app/cinema_detail.html'
    context_object_name = 'cinema_view'

    def get_context_data(self, **kwargs):
        ctx = super(CinemaDetail, self).get_context_data(**kwargs)
        ctx['title'] = Cinema.objects.get(slug=self.kwargs['slug'])
        return ctx


class HallDetail(DetailView):
    model = Hall
    template_name = 'movie_app/hall_detail.html'
    context_object_name = 'hall_view'

    def get_context_data(self, **kwargs):
        ctx = super(HallDetail, self).get_context_data(**kwargs)
        ctx['title'] = Hall.objects.get(pk=self.kwargs['pk'])
        return ctx


class NewsList(ListView):
    model = News
    template_name = 'movie_app/news_list.html'
    context_object_name = 'news'
    extra_context = {'title': 'Новости'}


class ActionsList(ListView):
    model = Action
    template_name = 'movie_app/actions_list.html'
    context_object_name = 'actions'
    extra_context = {'title': 'Акции'}


class ActionDetail(DetailView):
    model = Action
    template_name = 'movie_app/action_detail.html'
    context_object_name = 'action_view'

    def get_context_data(self, **kwargs):
        ctx = super(ActionDetail, self).get_context_data(**kwargs)
        ctx['title'] = Action.objects.get(pk=self.kwargs['pk'])
        return ctx


class ContactList(ListView):
    model = Contacts
    template_name = 'movie_app/contacts.html'
    context_object_name = 'contacts'
    extra_context = {'title': 'Контакты кинотеатров'}

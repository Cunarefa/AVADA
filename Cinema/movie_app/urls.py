from django.urls import path

from .views import *

urlpatterns = [
    path('', AllMovies.as_view(), name='main'),
    path('registration/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('movie/<str:slug>/', MovieView.as_view(), name='movie_detail'),
    path('afisha/', AfishaView.as_view(), name='afisha'),
    path('cinema-all/', CinemaListView.as_view(), name='cinema_all'),
    path('cinema/<str:slug>/', CinemaDetail.as_view(), name='cinema_item'),
    path('hall/<int:pk>/', HallDetail.as_view(), name='hall_item'),
    path('news/', NewsList.as_view(), name='news_list'),
    path('actions/', ActionsList.as_view(), name='action_list'),
    path('action/<int:pk>/detail/', ActionDetail.as_view(), name='action_item'),
    path('сontacts/', ContactList.as_view(), name='cinema_contacts'),
    path('cafe/', CafeView.as_view(), name='cafe_view'),
]

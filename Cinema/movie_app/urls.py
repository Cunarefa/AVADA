from django.urls import path

from .views import *

urlpatterns = [
    path('', Unreleased.as_view(), name='main'),
    path('registration/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('movie/<str:slug>/', MovieView.as_view(), name='movie_detail'),
    path('afisha/', AfishaView.as_view(), name='afisha'),
    path('cinema-all/', CinemaListView.as_view(), name='cinema_all'),
]

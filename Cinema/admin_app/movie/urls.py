from django.urls import path

from .views import *


urlpatterns = [
    path('', admin_app, name='admin'),
    path('movies/', AdminAllMoviesList.as_view(), name='admin_movies'),
    path('movie/create/', create_movie, name='add_movie'),
    # path('movie/create/', AdminCreateMovie.as_view(), name='add_movie'),
    path('movie/update/<str:slug>/', AdminUpdateMovie.as_view(), name='update_movie'),
    path('movie/delete/<str:slug>/', AdminDeleteMovie.as_view(), name='delete_movie'),
]



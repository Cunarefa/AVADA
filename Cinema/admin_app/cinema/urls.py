from django.urls import path

from .views import AdminCinemaListView, CreateCinemaAdmin, UpdateCinemaAdmin, DeleteCinemaAdmin

urlpatterns = [
    path('cinema/', AdminCinemaListView.as_view(), name='cinemas'),
    path('cinema/create/', CreateCinemaAdmin.as_view(), name='create_cinema'),
    path('cinema/update/<str:slug>/', UpdateCinemaAdmin.as_view(), name='update_cinema'),
    path('cinema/delete/<str:slug>/', DeleteCinemaAdmin.as_view(), name='delete_cinema'),
]
from django.urls import path

from admin_app.hall.views import CreateHallView, UpdateHallView, DeleteHall

urlpatterns = [
    path('hall/create/', CreateHallView.as_view(), name='create_hall'),
    path('hall/update/<int:pk>/', UpdateHallView.as_view(), name='hall_detail'),
    path('hall/delete/<int:pk>/', DeleteHall.as_view(), name='delete_hall'),
]
from django.urls import path

from admin_app.users.views import UserList, UpdateUser, delete_user, change_password

urlpatterns = [
    path('users/', UserList.as_view(), name='users_list'),
    path('user/<int:pk>/update/', UpdateUser.as_view(), name='update_user'),
    path('user/<int:pk>/delete', delete_user, name='delete_user'),
    path('user/change-password/', change_password, name='change_pass'),
]

from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView

from admin_app.users.forms import UserUpdateForm, ChangePassword
from movie_app.models import User


class UserList(ListView):
    model = User
    template_name = 'users/users_list.html'
    context_object_name = 'users'
    extra_context = {'title': 'Пользователи'}


class UpdateUser(UpdateView):
    model = User
    template_name = 'users/update_user.html'
    form_class = UserUpdateForm
    context_object_name = 'update_user'
    extra_context = {'title': 'Редактировать пользователя'}
    success_url = reverse_lazy('users_list')


def delete_user(request, pk):
    User.objects.filter(pk=pk).delete()
    return redirect('users_list')


def change_password(request):
    if request.method == 'POST':
        form = ChangePassword(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, 'Your password was successfully updated!')
            return redirect('update_user')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = ChangePassword(user=request.user)

    context = {
        'form': form,
        'title': 'Изменить пароль'
    }
    return render(request, 'users/change_pass.html', context)

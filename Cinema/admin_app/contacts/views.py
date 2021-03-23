from django.urls import reverse_lazy
from django.views.generic import ListView, DeleteView, CreateView

from admin_app.contacts.forms import ContactsForm
from movie_app.models import Contacts


class ContactListAdmin(ListView):
    model = Contacts
    template_name = 'contacts/contacts_list.html'
    context_object_name = 'contacts'
    extra_context = {'title': 'Список контактов'}


class CreateContact(CreateView):
    model = Contacts
    form_class = ContactsForm
    template_name = 'contacts/create_cinema_contacts.html'
    success_url = reverse_lazy('contacts_list')
    extra_context = {'title': 'Создать данные для к-ра'}


class DeleteContactAdmin(DeleteView):
    model = Contacts
    template_name = 'admin_app/delete.html'
    success_url = reverse_lazy('contacts_list')

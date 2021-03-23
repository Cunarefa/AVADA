from django.urls import path

from .views import ContactListAdmin, DeleteContactAdmin, CreateContact

urlpatterns = [
    path('contacts/', ContactListAdmin.as_view(), name='contacts_list'),
    path('contact/create/', CreateContact.as_view(), name='create_contact'),
    path('contact/<int:pk>/delete/', DeleteContactAdmin.as_view(), name='delete_contact'),
]
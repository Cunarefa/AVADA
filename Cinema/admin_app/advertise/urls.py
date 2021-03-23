from django.urls import path

from admin_app.advertise.views import AdminAdvertiseListView, CreateAdvertiseAdmin, DetailAdvertiseAdmin

urlpatterns = [
    path('advertise/', AdminAdvertiseListView.as_view(), name='advertise_list'),
    path('advertise/create/', CreateAdvertiseAdmin.as_view(), name='create_advertise'),
    path('advertise/<int:pk>/detail/', DetailAdvertiseAdmin.as_view(), name='advertise_detail'),
]

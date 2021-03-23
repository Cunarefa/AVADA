from django.urls import path

from admin_app.kids_room.views import AdminKidsRoomListView, CreateKidsRoomAdmin, DetailKidsRoomAdmin

urlpatterns = [
    path('kids_rooms/', AdminKidsRoomListView.as_view(), name='kids_rooms_list'),
    path('kids_room/create/', CreateKidsRoomAdmin.as_view(), name='create_kids_room'),
    path('kids_room/<int:pk>/detail/', DetailKidsRoomAdmin.as_view(), name='kids_room_detail'),
]

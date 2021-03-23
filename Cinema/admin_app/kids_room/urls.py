from django.urls import path

from admin_app.vip_hall.views import AdminVipHallListView, CreateVipHallAdmin, DetailVipHallAdmin

urlpatterns = [
    path('vip_halls/', AdminVipHallListView.as_view(), name='vip_halls_list'),
    path('vip_hall/create/', CreateVipHallAdmin.as_view(), name='create_vip'),
    path('vip_hall/<int:pk>/detail/', DetailVipHallAdmin.as_view(), name='vip_detail'),
]

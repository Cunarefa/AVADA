from django.urls import path

from admin_app.cafe.views import AdminCafeListView, CreateCafeAdmin, DetailCafeAdmin

urlpatterns = [
    path('cafe/', AdminCafeListView.as_view(), name='cafe_list'),
    path('cafe/create/', CreateCafeAdmin.as_view(), name='create_cafe'),
    path('cafe/<int:pk>/detail/', DetailCafeAdmin.as_view(), name='cafe_detail'),
]

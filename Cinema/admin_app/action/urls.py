from django.urls import path

from admin_app.action.views import AdminActionListView, CreateActionAdmin, DetailActionAdmin

urlpatterns = [
    path('actions/', AdminActionListView.as_view(), name='actions'),
    path('action/create/', CreateActionAdmin.as_view(), name='create_action'),
    path('action/<int:pk>/detail/', DetailActionAdmin.as_view(), name='action_detail'),
]

from django.urls import path

from admin_app.news.views import AdminNewsListView, CreateNewsAdmin, DetailNewsAdmin

urlpatterns = [
    path('news/', AdminNewsListView.as_view(), name='news'),
    path('news/create/', CreateNewsAdmin.as_view(), name='create_news'),
    path('news/<int:pk>/detail/', DetailNewsAdmin.as_view(), name='detail_news'),
]
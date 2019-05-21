from django.urls import path

from bookmark.views import BookmarkListView
from . import views

app_name = 'bookmark'

urlpatterns = [
    # ex: /polls/
    # path('', views.IndexView.as_view(), name='index'),
    path('', BookmarkListView.as_view(), name='list'),
]
from django.urls import path

from bookmark.views import BookmarkListView, BookmarkCreateView, BookmarkDetailView, BookmarkUpdateView, \
    BookmarkDeleteView
from . import views

app_name = 'bookmark'  #  app_name 을 사용하면 뷰에서 reverse_lazy(app_name:view_name)형식으로 호출해야한다.

urlpatterns = [
    # ex: /polls/
    # path('', views.IndexView.as_view(), name='index'),
    path(r'', BookmarkListView.as_view(), name='list'),
    path(r'add/', BookmarkCreateView.as_view(), name='add'),
    path(r'detail/<int:pk>/', BookmarkDetailView.as_view(), name='detail'),
    path(r'update/<int:pk>/', BookmarkUpdateView.as_view(), name='update'),
    path(r'delete/<int:pk>/', BookmarkDeleteView.as_view(), name='delete'),
]
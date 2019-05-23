from django.urls import path

from bookmark.views import BookmarkListView, BookmarkCreateView
from . import views

# app_name = 'bookmark'  # 이게 붙으니까 뷰에서 reverse_lazy()가 되지않는다.

urlpatterns = [
    # ex: /polls/
    # path('', views.IndexView.as_view(), name='index'),
    path(r'', BookmarkListView.as_view(), name='list'),
    path(r'add/', BookmarkCreateView.as_view(), name='add'),
]
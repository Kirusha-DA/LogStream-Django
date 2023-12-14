from django.urls import path
from .views import NewsListView, NewsCreateView, NewsUpdateView
from .views import BlogDetailView, BlogsListView

urlpatterns = [
    path("", NewsListView.as_view(), name="news"),
    path("news/new/", NewsCreateView.as_view(), name ="post_news"),
    path("news/<int:pk>/edit", NewsUpdateView.as_view(), name="edit_news"),
    path("blogs/<int:pk>", BlogDetailView.as_view(), name="blog_detail"),
    path("blogs/", BlogsListView.as_view(), name="blogs"),
]
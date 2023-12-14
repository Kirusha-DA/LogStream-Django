from .models import News, Blog

from django.views.generic import ListView, DetailView, UpdateView
from django.views.generic.edit import CreateView



class NewsListView(ListView):
    model = News
    paginate_by = 5
    template_name = "newssite/news/list.html"


class NewsCreateView(CreateView):
    model = News
    template_name = "newssite/news/post.html";
    fields = ["title", "text", "image", "blog"]


class NewsUpdateView(UpdateView):
    model = News
    template_name = "newssite/news/edit.html"
    fields = ["title", "text", "image", "blog"]


class BlogsListView(ListView):
    model = Blog
    template_name = "newssite/blogs/list.html" 


class BlogDetailView(DetailView):
    model = Blog
    template_name = "newssite/blogs/detail.html"
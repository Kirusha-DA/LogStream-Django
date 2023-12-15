from django.forms.models import BaseModelForm
from django.http import HttpResponse
from .models import News, Blog

from django.views.generic import ListView, DetailView, UpdateView
from django.views.generic.edit import CreateView

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

class NewsListView(ListView):
    model = News
    paginate_by = 5
    template_name = "newssite/news/list.html"


class NewsCreateView(LoginRequiredMixin,UserPassesTestMixin, CreateView):
    model = News
    template_name = "newssite/news/post.html";
    fields = ["title", "text", "image", "blog"]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        return self.request.user.username == "admin"


class NewsUpdateView(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
    model = News
    template_name = "newssite/news/edit.html"
    fields = ["title", "text", "image", "blog"]

    def test_func(self):
        obj = self.get_object()
        return obj.blog.author == self.request.user


class BlogsListView(ListView):
    model = Blog
    template_name = "newssite/blogs/list.html" 


class BlogDetailView(DetailView):
    model = Blog
    template_name = "newssite/blogs/detail.html"
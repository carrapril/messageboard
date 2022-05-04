from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from .models import Post 


class HomePageView(ListView):
    model = Post
    template_name = 'home.html'

class PostListView(ListView):
    template_name = 'posts/list.html'
    model = Post

class PostDetailView(DetailView):
    template_name = 'posts/detail.html'
    model = Post    

class PostCreateView(CreateView):
    template_name = 'posts/new.html'
    model = Post
    fields = ['title', 'body']
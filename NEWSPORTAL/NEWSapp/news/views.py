from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post
from datetime import datetime


class PostList(ListView):
    model = Post
    ordering = 'title'
    template_name = 'articles.html'
    context_object_name = 'Posts'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        context['next_sale'] = 'Распродажа НИКОГДА!'
        return context


# Create your views here.
class PostDetail(DetailView):
    model = Post
    template_name = 'article.html'
    context_object_name = 'post'
# Create your views here.

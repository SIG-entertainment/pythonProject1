from django.shortcuts import render
from NewsApp.models import Post
from NewsApp.models import Author
from NewsApp.models import Comment
from NewsApp.models import PostCategory
from NewsApp.models import Category
from django.views.generic import ListView, DetailView

class AuthorList(ListView):
    model = Author
    context_object_name = 'Authors'
    template_name = 'NewsApp/authors_list.html'

class PostDetail(DetailView):
    model = Post
    context_object_name = 'Post'

class PostList(ListView):
    model = Post
    context_object_name = 'Posts'
    template_name = 'NewsApp/post_list.html'
    ordering = '-dateCreation'


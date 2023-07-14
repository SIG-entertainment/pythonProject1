from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('authorlist/', AuthorList.as_view()),
    path('news/<int:pk>/', PostDetail.as_view(), name='Post'),
    path('news/', PostList.as_view(), name='post_list'),
    path('news/search/', SearchList.as_view()),

    path('news/create/', PostCreate.as_view()),
    path('news/<int:pk>/edit/', PostEdit.as_view()),
    path('news/<int:pk>/delete/', PostDelete.as_view()),

    path('articles/create/', ArticleCreate.as_view()),
    path('articles/<int:pk>/edit/', ArticleEdit.as_view()),
    path('articles/<int:pk>/delete/', ArticleDelete.as_view()),
]
from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('authorlist/', AuthorList.as_view()),
    path('news/<int:pk>/', PostDetail.as_view(), name='Post'),
    path('news/', PostList.as_view(), name='post_list'),
    path('news/search/', SearchList.as_view()),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('accounts.urls')),

    path('news/create/', PostCreate.as_view(), name='create_news'),
    path('news/<int:pk>/edit/', PostEdit.as_view(), name='edit_news'),
    path('news/<int:pk>/delete/', PostDelete.as_view(), name='delete_news'),

    path('articles/create/', ArticleCreate.as_view(), name='create_article'),
    path('articles/<int:pk>/edit/', ArticleEdit.as_view(), name='edit_article'),
    path('articles/<int:pk>/delete/', ArticleDelete.as_view(), name='delete_article'),

    path('categories/<int:pk>/', CategoryListView.as_view(), name='category_list'),
    path('categories/<int:pk>/subscribe/', subscribe, name='subscribe'),
]
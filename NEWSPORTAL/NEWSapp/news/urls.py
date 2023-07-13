from django.urls import path
from .views import PostList, PostDetail
from django.contrib import admin


urlpatterns = [
    path('news_list/', PostList.as_view()),
    path('<int:pk>', PostDetail.as_view()),
]
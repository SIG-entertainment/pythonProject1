from django.urls import path
from .views import PostList, PostDetail

urlpatterns = [
    path('news', PostList.as_view()),
    path('<int:pk>', PostDetail.as_view()),
]
from django.contrib import admin
from NewsApp.models import Author
from NewsApp.models import Category
from NewsApp.models import Post
from NewsApp.models import PostCategory
from NewsApp.models import Comment


admin.site.register(Author)
admin.site.register(Post)
admin.site.register(Category)
admin.site.register(PostCategory)
admin.site.register(Comment)

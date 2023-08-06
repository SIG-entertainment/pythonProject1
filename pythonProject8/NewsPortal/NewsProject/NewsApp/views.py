from django.shortcuts import render, get_object_or_404
from NewsApp.models import Post
from NewsApp.models import Author
from NewsApp.models import Comment
from NewsApp.models import PostCategory
from NewsApp.models import Category
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .filters import PostFilter
from django_filters import FilterSet
from .forms import PostForm, ArticleForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Exists, OuterRef
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect



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
    paginate_by = 5


class SearchList(PostList):
    template_name = 'NewsApp/search_list.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context


class PostCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = ('NewsApp.create_news',)
    raise_exception = True
    form_class = PostForm
    model = Post
    template_name = 'post_create.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.categoryType = 'HW'
        post.save()
        return super().form_valid(form)


class ArticleCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = ('NewsApp.create_article',)
    raise_exception = True
    form_class = ArticleForm
    model = Post
    template_name = 'article_create.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.categoryType = 'AR'
        post.save()
        return super().form_valid(form)


class PostEdit(PermissionRequiredMixin, UpdateView):
    permission_required = ('NewsApp.edit_news',)
    form_class = PostForm
    model = Post
    template_name = 'post_edit.html'


class ArticleEdit(PermissionRequiredMixin, UpdateView):
    permission_required = ('NewsApp.edit_news',)
    form_class = ArticleForm
    model = Post
    template_name = 'article_edit.html'


class PostDelete(PermissionRequiredMixin, DeleteView):
    permission_required = ('NewsApp.delete_news',)
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('post_list')


class ArticleDelete(PermissionRequiredMixin, DeleteView):
    permission_required = ('NewsApp.delete_news',)
    model = Post
    template_name = 'article_delete.html'
    success_url = reverse_lazy('post_list')


class CategoriesList(ListView):
    model = Category
    template_name = 'NewsApp/category_list_2.html'
    context_object_name = 'category_news_list'


class CategoryListView(ListView):
    model = Post
    template_name = 'NewsApp/category_list.html'
    context_object_name = 'category_news_list'

    def get_queryset(self):
        self.category = get_object_or_404(Category, id=self.kwargs['pk'])
        queryset = Post.objects.filter(postCategory=self.category).order_by('-dateCreation')
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_not_subscriber'] = self.request.user not in self.category.subscribers.all()
        context['category'] = self.category
        return context

@login_required
def subscribe(request, pk):
    user = request.user
    category = Category.objects.get(id=pk)
    category.subscribers.add(user)
    message = 'You successfully subscribed!'
    return render(request, 'subscribe.html', {'category': category, 'message': message})

# @login_required
# @csrf_protect
# def subscriptions(request):
#     if request.method == 'POST':
#         category_id = request.POST.get('category_id')
#         category = Category.objects.get(id=category_id)
#         action = request.POST.get('action')
#
#         if action == 'subscribe':
#             Subscription.objects.create(user=request.user, category=category)
#         elif action == 'unsubscribe':
#             Subscription.objects.filter(
#                 user=request.user,
#                 category=category,
#             ).delete()
#
#     categories_with_subscriptions = Category.objects.annotate(
#         user_subscribed=Exists(
#             Subscription.objects.filter(
#                 user=request.user,
#                 category=OuterRef('pk'),
#             )
#         )
#     ).order_by('name')
#     return render(
#         request,
#         'subscriptions.html',
#         {'categories': categories_with_subscriptions},
#     )
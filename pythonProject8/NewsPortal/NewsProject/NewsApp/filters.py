from django_filters import FilterSet, ModelMultipleChoiceFilter, CharFilter, IsoDateTimeFilter
from .models import Post, Category
from django.forms import DateTimeInput


class PostFilter(FilterSet):
   category = ModelMultipleChoiceFilter(
       field_name='postCategory',
       queryset=Category.objects.all(),
       label='Category',
   )

   title = CharFilter(
       field_name='title',
       lookup_expr='icontains',
       label='Title',
   )

   date = IsoDateTimeFilter(
       field_name='dateCreation',
       lookup_expr='gte',
       label='Ceation Date',
       widget=DateTimeInput(
           format='%Y-%m-%d',
           attrs={'type': 'datetime-local'}
       ),
   )






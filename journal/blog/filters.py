import django_filters

from .models import Post


class PostFilter(django_filters.FilterSet):
    tags__slug = django_filters.CharFilter(
        field_name='tags__slug', lookup_expr='exact',
    )

    class Meta:
        model = Post
        fields = ['tags__slug']

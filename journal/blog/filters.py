import django_filters
from .models import Post, Tag


class PostFilter(django_filters.FilterSet):
    tags = django_filters.ModelMultipleChoiceFilter(
        field_name='tags__slug',
        to_field_name='slug',
        queryset=Tag.objects.all(),
    )

    class Meta:
        model = Post
        fields = []

    def filter_queryset(self, queryset):
        tags_value = self.data.get('tags')

        if tags_value and 'without' in tags_value:
            return queryset.filter(tags__isnull=True)
        else:
            return super().filter_queryset(queryset)

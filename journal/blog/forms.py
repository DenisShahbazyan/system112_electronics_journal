from django import forms

from .models import Post, Tag


class PostForm(forms.ModelForm):
    """Форма для создания и редактирования постов."""
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        label='Теги',
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["text"].required = False
        self.fields["tags"].required = False

    class Meta:
        model = Post
        fields = ('text', 'tags',)

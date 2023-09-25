from urllib.parse import urlparse

from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required

from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from .forms import PostForm
from .models import Post, Tag
from .utils import include_paginator, search_posts, get_request_GET_params
from .filters import PostFilter

User = get_user_model()


@login_required
def index(request):
    posts = PostFilter(request.GET, queryset=Post.objects.all()).qs
    posts = search_posts(request, posts)
    posts_paginator = include_paginator(request, posts)
    tags = Tag.objects.all()

    return render(
        request=request,
        template_name='blog/index.html',
        context={
            'posts_paginator': posts_paginator,
            'tags': tags,
            'get_params': get_request_GET_params(request, ('tags', 'q')),
        },
    )


@login_required
def profile(request, username):
    author = get_object_or_404(User, username=username)
    count_posts = author.posts.all().count()
    posts = author.posts.all()
    posts_paginator = include_paginator(request, posts)
    tags = Tag.objects.all()

    return render(
        request=request,
        template_name='blog/profile.html',
        context={
            'author': author,
            'count_posts': count_posts,
            'posts_paginator': posts_paginator,
            'tags': tags,
        }
    )


@login_required
def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    author = post.author
    count_posts = author.posts.all().count()
    referer = request.META.get('HTTP_REFERER')

    return render(
        request=request,
        template_name='blog/post_detail.html',
        context={
            'count_posts': count_posts,
            'post': post,
            'referer': referer,
        }
    )


@login_required
def post_create(request):
    form = PostForm(
        request.POST or None,
        files=request.FILES or None
    )
    if form.is_valid():
        post = form.save(commit=False)
        post.author = request.user
        post.save()

        post.tags.clear()
        post.tags.set(form.cleaned_data['tags'])
        return redirect('blog:profile', request.user.username)
    return render(
        request=request,
        template_name='blog/create_post.html',
        context={
            'form': form
        }
    )


@login_required
def post_edit(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if post.author != request.user:
        return redirect('blog:post_detail', post.id)

    form = PostForm(
        request.POST or None,
        files=request.FILES or None,
        instance=post
    )
    if form.is_valid():
        post = form.save(commit=False)
        post.author = request.user
        post.save()

        post.tags.clear()
        post.tags.set(form.cleaned_data['tags'])
        return redirect('blog:post_detail', post.id)

    return render(
        request=request,
        template_name='blog/create_post.html',
        context={
            'is_edit': True,
            'post': post,
            'form': form,
        }
    )


@login_required
def post_delete(request, post_id, referer):
    post = get_object_or_404(Post, pk=post_id)
    if post.author != request.user:
        return redirect(referer, post.id)

    redirect_url = referer
    referer = urlparse(referer).path

    post_url = reverse('blog:post_detail', args=[post_id]) + 'edit/'

    if referer == post_url or referer == 'None':
        redirect_url = reverse('blog:index')

    post.delete()
    return redirect(redirect_url, post.id)

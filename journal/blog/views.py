from urllib.parse import urlparse

from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from .forms import PostForm
from .models import Post
from .utils import include_paginator

User = get_user_model()


@login_required
def index(request):
    search_query = request.GET.get('q', '')
    if search_query:
        search_terms = search_query.split()
        q_objects = Q()
        for term in search_terms:
            q_objects |= (
                Q(text__icontains=term) |
                Q(author__first_name__icontains=term) |
                Q(author__last_name__icontains=term) |
                Q(author__patronymic__icontains=term) |
                Q(author__username__icontains=term)
            )
        posts = Post.objects.filter(q_objects)
    else:
        posts = Post.objects.all()
    posts_paginator = include_paginator(request, posts)

    return render(
        request=request,
        template_name='blog/index.html',
        context={
            'posts_paginator': posts_paginator,
        },
    )


@login_required
def profile(request, username):
    author = get_object_or_404(User, username=username)
    count_posts = author.posts.all().count()
    posts = author.posts.all()
    posts_paginator = include_paginator(request, posts)

    return render(
        request=request,
        template_name='blog/profile.html',
        context={
            'author': author,
            'count_posts': count_posts,
            'posts_paginator': posts_paginator,
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

from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404, redirect, render


from .models import Post
from .utils import include_paginator
from .forms import PostForm


User = get_user_model()


@login_required
def index(request):
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

    return render(
        request=request,
        template_name='blog/post_detail.html',
        context={
            'count_posts': count_posts,
            'post': post,
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
    return render(request, 'blog/create_post.html', {'form': form})


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

from django.urls import path
from django.urls import re_path

from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.index, name='index'),
    path('profile/<str:username>/', views.profile, name='profile'),
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),
    path('post_create/', views.post_create, name='post_create'),
    path('post/<int:post_id>/edit/', views.post_edit, name='post_edit'),
    re_path(
        r'post_delete/(?P<post_id>[0-9]+)/(?P<referer>.+)/$',
        views.post_delete,
        name='post_delete'
    ),
]

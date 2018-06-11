from django.conf.urls import url, include
from django.views.generic import ListView, DetailView
from forum.models import Post, Comment

from . import views

urlpatterns = [
    url(r'^$', views.forumListView.as_view(), name='post_list'),
    url(r'^(?P<pk>\d+$)', DetailView.as_view(model=Post, template_name='forum/post.html'))
]

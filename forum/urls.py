from django.urls import re_path
from django.views.generic import ListView, DetailView
from forum.models import Post, Comment

from . import views

urlpatterns = [
    re_path(r'^$', views.post_list, name='post_list'),
    re_path(r'^(?P<pk>\d+)/$', views.post_detail, name='post_detail')
    #url(r'^(?P<pk>\d+$)', DetailView.as_view(model=Post, template_name='forum/post.html'))
]

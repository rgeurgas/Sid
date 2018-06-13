from django.urls import re_path
from django.views.generic import ListView, DetailView
from forum.models import Post, Comment

from . import views

urlpatterns = [
    re_path(r'^$', views.post_list, name='post_list'),
    re_path(r'^(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    re_path(r'^new/$', views.post_new, name='post_new'),
    re_path(r'^(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
    re_path(r'^(?P<pk>\d+)/remove/$', views.post_remove, name='post_remove'),
    re_path(r'^\d/(?P<pk>\d+)/remove$', views.comment_remove, name='comment_remove')
]

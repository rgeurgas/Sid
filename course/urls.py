"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import re_path

from course import views

urlpatterns = [
    re_path(r'^$', views.home, name='home'),
    re_path(r'^course-search$', views.course_search, name='course_search'),
    re_path(r'^courses$', views.course_list, name='course_list'),
    re_path(r'^course/(?P<pk>\d+)/$', views.course_details, name='course_details'),
    
    re_path(r'^links/$', views.link_list, name='link_list'),
    re_path(r'^links/(?P<pk>\d+)/$', views.link_detail, name='link_detail'),
    re_path(r'^links/(?P<pk>\d+)/remove/$', views.link_remove, name='link_remove'),
    
    re_path(r'^lists/$', views.list_list, name='list_list'),
    re_path(r'^lists/(?P<pk>\d+)/$', views.list_detail, name='list_detail'),
    re_path(r'^lists/(?P<pk>\d+)/remove/$', views.list_remove, name='list_remove'),
    
    re_path(r'^summaries/$', views.summary_list, name='summary_list'),
    re_path(r'^summaries/(?P<pk>\d+)/$', views.summary_detail, name='summary_detail'),
    re_path(r'^summaries/(?P<pk>\d+)/remove/$', views.summary_remove, name='summary_remove'),

    re_path(r'^course/(?P<course_pk>\d+)/forum/$', views.post_list, name='post_list'),
    re_path(r'^course/(?P<course_pk>\d+)/forum/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    re_path(r'^course/(?P<course_pk>\d+)/forum/new/$', views.post_new, name='post_new'),
    re_path(r'^course/(?P<course_pk>\d+)/forum /(?P<pk>\d+)/remove/$', views.post_remove, name='post_remove'),
    re_path(r'^course/(?P<course_pk>\d+)/forum/(?P<post_pk>\d+)/(?P<pk>\d+)/remove$', views.comment_remove, name='comment_remove')
]

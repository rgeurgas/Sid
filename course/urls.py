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
    re_path(r'^course/(?P<pk>\d+)/$', views.course_details, name='course_details'),

    re_path(r'^links/(?P<pk>\d+)/remove/$', views.link_remove, name='link_remove'),
    
    re_path(r'^lists/(?P<pk>\d+)/remove/$', views.list_remove, name='list_remove'),
    
    re_path(r'^summaries/(?P<pk>\d+)/remove/$', views.summary_remove, name='summary_remove'),

    re_path(r'^course/(?P<course_pk>\d+)/forum/$', views.post_list, name='post_list'),
    re_path(r'^course/(?P<course_pk>\d+)/forum/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    re_path(r'^course/(?P<course_pk>\d+)/forum /(?P<pk>\d+)/remove/$', views.post_remove, name='post_remove'),
    re_path(r'^course/(?P<course_pk>\d+)/forum/(?P<post_pk>\d+)/(?P<pk>\d+)/remove$', views.comment_remove, name='comment_remove'),

    re_path(r'^course/(?P<course_pk>\d+)/links/$', views.course_all_links, name='links_see_more'),
    re_path(r'^course/(?P<course_pk>\d+)/lists/$', views.course_all_lists, name='lists_see_more'),
    re_path(r'^course/(?P<course_pk>\d+)/summaries/$', views.course_all_summaries, name='summaries_see_more'),

    re_path(r'^course/(?P<course_pk>\d+)/sub/$', views.course_sub, name='course_sub'),
    re_path(r'^course/(?P<course_pk>\d+)/unsub/$', views.course_unsub, name='course_unsub'),
]

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
    re_path(r'^$', views.course_list, name='course_list'),
    re_path(r'^course/new/$', views.course_new, name='course_new'),
    re_path(r'^course/(?P<pk>\d+)/$', views.course_details, name='course_details'),
    re_path(r'^course/(?P<pk>\d+)/edit/$', views.course_edit, name='course_edit'),
    
    re_path(r'^link_add/$', views.link_add, name='link_add'),
    re_path(r'^links/$', views.link_list, name='link_list'),
    re_path(r'^links/(?P<pk>\d+)', views.link_detail, name='link_detail'),
    
    re_path(r'^list_add/$', views.list_add, name='list_add'),
    re_path(r'^lists/$', views.list_list, name='list_list'),
    re_path(r'^lists/(?P<pk>\d+)', views.list_detail, name='list_detail'),
    
    re_path(r'^summary_add/$', views.summary_add, name='summary_add'),
    re_path(r'^summaries/$', views.summary_list, name='summary_list'),
	re_path(r'^summaries/(?P<pk>\d+)', views.summary_detail, name='summary_detail'),
]

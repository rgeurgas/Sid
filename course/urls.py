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

from . import views

urlpatterns = [
	re_path(r'^$', views.course_list, name='course_list'),
    re_path(r'^new/$', views.course_new, name='course_new'),
    re_path(r'^(?P<pk>\d+)/$', views.course_details, name='course_details'),
    re_path(r'^(?P<pk>\d+)/edit/$', views.course_edit, name='course_edit'),
    re_path(r'^(?P<pk>\d+)/remove/$', views.course_remove, name='course_remove'),
]

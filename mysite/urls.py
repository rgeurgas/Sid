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
from django.contrib import admin
from django.urls import re_path, include
from django.conf import settings

from course import views

urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^', include('course.urls'), name='course'),
    re_path(r'^auth/', include('registration.urls'), name='auth'),
    re_path(r'^forum/', include('forum.urls'), name='forum'),
    re_path(r'^media/(?P<path>uploads/[0-9]{4}/[0-9]{2}/[0-9]{2}/.{1,100})', views.download, name='downloads'),
    
]

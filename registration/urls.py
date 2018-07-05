from django.urls import re_path, include

from registration import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    re_path(r'^login/$', auth_views.login, name='login'),
    re_path(r'^logout/$', auth_views.logout, {'next_page': '/'}, name='logout'),
    re_path(r'^signup/$', views.signup, name='signup'),
    re_path(r'^profile/(?P<pk>\d+)$', views.view_profile, name='view_profile'),
    re_path(r'^profile/(?P<pk>\d+)$', views.view_profile, name='edit_profile'),
    re_path(r'^approve', views.approve_and_close, name='approve_and_close')
]

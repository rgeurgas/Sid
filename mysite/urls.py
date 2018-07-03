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
from django.conf.urls.static import static
from django.conf.urls import include, url

from importlib import import_module
from allauth.socialaccount import providers
from allauth import app_settings

from course import views


urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^', include('course.urls'), name='course'),
    re_path(r'^auth/', include('registration.urls'), name='auth'),
    re_path(r'^media/(?P<path>uploads/[0-9]{4}/[0-9]{2}/[0-9]{2}/.{1,100})', views.download, name='downloads'),
    re_path(r'^/', include('allauth.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if app_settings.SOCIALACCOUNT_ENABLED:
    urlpatterns += [url(r'^social/', include('allauth.socialaccount.urls'))]

for provider in providers.registry.get_list():
    try:
        prov_mod = import_module(provider.get_package() + '.urls')
    except ImportError:
        continue
    prov_urlpatterns = getattr(prov_mod, 'urlpatterns', None)
    if prov_urlpatterns:
        urlpatterns += prov_urlpatterns

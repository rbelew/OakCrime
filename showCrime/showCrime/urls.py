"""showCrime URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.urls import include
from django.urls import re_path as url

from django.contrib import admin
from django.contrib.staticfiles import views as static_views

from rest_framework import routers

from .views import health

from django.conf import settings

urlpatterns = [
    url(r'', include('dailyIncid.urls')),
    url(r'^dailyIncid/', include('dailyIncid.urls')),
	url(r'^health/', health, name='health'),
	
	url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
	
    url(r'^admin/', admin.site.urls),
]
if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        # For django versions before 3.0:
        url(r'^__debug__/', include(debug_toolbar.urls)),

        # Serve static files in development
        url(r'^static/(?P<path>.*)$', static_views.serve),
    ] + urlpatterns

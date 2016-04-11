"""Teammer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from django.conf.urls import url
from django.conf.urls import include
from django.contrib.auth.forms import User
from django.contrib import admin
from Teammer.views import *
import psycopg2

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^index/', index),
    url(r'^login/', sign_in),
    url(r'^project/', project),
    url(r'^projects/', projects),
    url(r'^profile/', profile),
    url(r'^profile_edit/', profile_edit),
    url(r'^about/', about),
    url(r'^users/', users),
    url(r'^accounts/', include('allauth.urls')),
]
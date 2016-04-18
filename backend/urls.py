from django.conf.urls import url
from django.conf.urls import include
from django.contrib.auth.forms import User
from django.contrib import admin
from Teammer.views import *
import psycopg2

from backend.views import *

urlpatterns = [
    url(r'^$', index),
    url(r'^login/', sign_in),
    url(r'^project/(?P<project_id>[0-9]+)/$', project),
    url(r'^apply_project/(?P<project_id>[0-9]+)/$', apply_project),
    url(r'^projects/', projects),
    url(r'^profile/(?P<user_id>[0-9]+)/$', profile),
    url(r'^profile_edit/', profile_edit),
    url(r'^create_project/', create_project),
    url(r'^register_project/', register_project),
    url(r'^about/', about),
    url(r'^users/', users),
]

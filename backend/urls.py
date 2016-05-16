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
    url(r'^apply_applicant/(?P<user_id>[0-9]+)/(?P<proj_id>[0-9]+)/$', apply_applicant),
    url(r'^apply_manage/(?P<project_id>[0-9]+)/$', apply_changes_manage_project),
    url(r'^manage_project/(?P<project_id>[0-9]+)/$', manage_project),
    url(r'^projects/', projects),
    url(r'^profile/(?P<user_id>[0-9]+)/$', profile),
    url(r'^profile_edit/(?P<user_id>[0-9]+)/$', profile_edit),
    url(r'^profile_edit/', profile_edit),
    url(r'^profile_apply_changes/(?P<user_id>[0-9]+)?$', profile_apply_changes),
    url(r'^create_project/', create_project),
    url(r'^register_project/', register_project),
    url(r'^about/', about),
    url(r'^logout/', logout),
    url(r'^users/', users),
]

from django.http import HttpResponse
from django.template.context_processors import csrf
from django.template.loader import get_template
from django.template import Context
import django.contrib.staticfiles
import django.db.backends.postgresql_psycopg2 as postgres
import datetime

def index(request):
    index_template = get_template('index.html')
    html = index_template.render()
    return HttpResponse(html)


def sign_in(request):
    signing_template = get_template('Sign_in.html')
    html = signing_template.render()
    return HttpResponse(html)


def project(request):
    project_template = get_template('Project.html')
    html = project_template.render()
    return HttpResponse(html)


def projects(request):
    projects_template = get_template('Projects.html')
    html = projects_template.render()
    return HttpResponse(html)


def about(request):
    about_template = get_template('About.html')
    html = about_template.render()
    return HttpResponse(html)


def profile(request):
    profile_template = get_template('Profile.html')
    html = profile_template.render()
    return HttpResponse(html)


def profile_edit(request):
    profile_logged_in = get_template('Profile_SignIn.html')
    html = profile_logged_in.render()
    return HttpResponse(html)


def users(request):
    users_template = get_template('Users.html')
    html = users_template.render()
    return HttpResponse(html)

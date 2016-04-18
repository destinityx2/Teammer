from django.contrib import auth
<<<<<<< HEAD
from django.contrib.auth.models import User
=======
>>>>>>> 9c6cabfc31199fe901be05d610bbbfaabab0bbe7
from django.http import HttpResponse
from django.shortcuts import render_to_response, redirect
from django.template.context_processors import csrf
from django.template.loader import get_template
<<<<<<< HEAD
=======


def index(request):
    index_template = get_template('index.html')
    html = index_template.render()
    return HttpResponse(html)


def sign_in(request):
    args = {}
    args.update(csrf(request))

    if request.POST:
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/admin')
        else:
            args['login_error'] = 'User not found'
            return render_to_response('Sign_in.html', args)
    else:
        return render_to_response('Sign_in.html', args)


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
>>>>>>> 9c6cabfc31199fe901be05d610bbbfaabab0bbe7

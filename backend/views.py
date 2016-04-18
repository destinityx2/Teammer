from django.contrib import auth
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render_to_response, redirect
from django.template.context_processors import csrf
from django.template.loader import get_template


def index(request):
    index_template = get_template('index.html')
    html = index_template.render()
    return HttpResponse(html)


def sign_in(request):
    args = {}
    args.update(csrf(request))

    if 'login' in request.POST:
        if request.POST:

            username = request.POST.get('username', '')
            password = request.POST.get('password', '')
            user = auth.authenticate(username=username, password=password)

            if user is not None:
                auth.login(request, user)
                print("success")
                return redirect('/admin')
            else:
                args['login_error'] = 'User not found'
                return render_to_response('Sign_in.html', args)
        else:
            return render_to_response('Sign_in.html', args)

    elif 'register' in request.POST:
        if request.POST:
            username = request.POST.get('usernamesignup', '')
            password = request.POST.get('passwordsignup', '')
            password_confirm = request.POST.get('passwordsignup_confirm', '')
            email = request.POST.get('emailsignup', '')

            print(username)
            print(password)
            print(password_confirm)
            print(email)

            if password == password_confirm:
                user = User.objects.create_user(username, email, password)
                user.save()
                return redirect('/index')
            else:
                return redirect('/login')
        else:
            return render_to_response('Sign_in.html', args)

    return render_to_response('Sign_in.html', args)


def create_project(request):
    create_project = get_template('CreateProject.html')
    html = create_project.render()
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

from django.contrib import auth
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render_to_response, redirect
from django.template.context_processors import csrf
from django.template.loader import get_template
from django.utils import timezone
from backend.models import UserInfo, ProjectUsers, Project


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
                userinfo = UserInfo(user = user)
                userinfo.save()
                print(user)
                return redirect('/index')
            else:
                return redirect('/login')
        else:
            return render_to_response('Sign_in.html', args)

    return render_to_response('Sign_in.html', args)


def create_project(request):
    args = {}
    args.update(csrf(request))
    return render_to_response('CreateProject.html', args)


def register_project(request, project_id=1):
    args = {}
    args.update(csrf(request))

    if request.POST:
        project_name = request.POST.get('project_name')
        description = request.POST.get('description')
        skills = request.POST.get('skills')
        num_members = request.POST.get('num_members')

        user = User.objects.filter(id=request.user.id)[0]

        proj = Project(project_name = project_name, description = description, skills = skills,
                   publication_date = timezone.now(), max_people = int(num_members))

        proj.creator = user

        proj.save()

    return render_to_response('index.html', args)


def project(request, project_id):
    args = {}
    # project_id = request.GET.get('id', '')
    project = Project.objects.filter(id=project_id)[0]

    if project is None:
        return redirect('/index')
    else:
        args['description'] = project.description
        args['max_number'] = project.max_people
        args['skills'] = project.skills

        participants = ProjectUsers.objects.filter(id=project_id)

        args['cur_number'] = len(participants)
        return render_to_response('Project.html', args)


def projects(request):
    args = {}
    args.update(csrf(request))
    projects = Project.objects.all()
    #print("XXX", projects[0])
    # projects = [Project()]
    #print(projects)

    # print(Project.objects.all())
    args.update({"projects": projects})
    return render_to_response('Projects.html', args)


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

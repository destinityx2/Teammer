from django.contrib import auth
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.template.context_processors import csrf
from django.template.loader import get_template
from django.utils import timezone
from backend.models import UserInfo, ProjectUsers, Project, Applicants


def index(request):
    return render_to_response('index.html', context_instance=RequestContext(request))


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
                return redirect('/index')
            else:
                args['login_error'] = 'User not found'
                return render_to_response('Sign_in.html', args, context_instance=RequestContext(request))
        else:
            return render_to_response('Sign_in.html', args, context_instance=RequestContext(request))

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
                userinfo = UserInfo(user=user)
                userinfo.save()
                print(user)
                return redirect('/index/login')
            else:
                return redirect('/index/login')
        else:
            return render_to_response('Sign_in.html', args, context_instance=RequestContext(request))

    return render_to_response('Sign_in.html', args, context_instance=RequestContext(request))


def create_project(request):
    args = {}
    args.update(csrf(request))
    return render_to_response('CreateProject.html', args, context_instance=RequestContext(request))


def register_project(request):
    project_id = 0
    args = {}
    args.update(csrf(request))

    print("HERE!!!")

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

        ProjectUsers(user=user, project = proj).save()
        project_id = proj.id

    return redirect('/index/project/{}/'.format(project_id))


def project(request, project_id):
    args = {}
    # project_id = request.GET.get('id', '')
    project = Project.objects.filter(id=project_id)[0]
    is_admin = False

    if project.creator == request.user:
        is_admin = True



    takes_part = False

    participants = ProjectUsers.objects.filter(project=project)

    ids = []

    for item in participants:
        ids.append(item.user.id)

    if request.user.id in ids or len(participants) == project.max_people:
        takes_part = True

    args['part'] = takes_part

    if project is None:
        return redirect('/index')
    else:
        args['description'] = project.description
        args['max_number'] = project.max_people
        args['skills'] = project.skills

        photos = []
        members = []

        for member in participants:
            photo = UserInfo.objects.filter(id=member.id)
            #user = User.objects.filter(id=member.id)
            user = member.user

            print("LOOKING FOR USER WITH ID", member.id)
            print("FOUND USER = ", user)

            print(member.id)
            if not photo:
                photos.append('img/user_default.png')
            else:
                photos.append(UserInfo.objects.filter(id=member.id)[0].photo)

            if user:
                members.append(user)

        if not members:
            print("MEMBERS ARE 0")

        args['members'] = members
        args['project_q'] = project
        args['photos'] = photos
        args['cur_number'] = len(participants)

        if not is_admin:
            return render_to_response('Project.html', args, context_instance=RequestContext(request))
        else:
            return render_to_response('Project_for_Creator.html', args, context_instance=RequestContext(request))


def apply_project(request, project_id):
    args = {}

    user = User.objects.filter(id=request.user.id)[0]

    current_num = len(ProjectUsers.objects.filter(project_id=project_id))
    max_num = (Project.objects.filter(id=project_id)[0]).max_people

    print(current_num, max_num)

    if current_num < max_num:
        #current_num += 1

        #new_instance = ProjectUsers()
        #new_instance.user = user
        #new_instance.project = Project.objects.filter(id=project_id)[0]

        #new_instance.save()

        new_applicant = Applicants()
        new_applicant.user = user
        new_applicant.project = Project.objects.filter(id=project_id)[0]

        new_applicant.save()

    return redirect('/index/projects/' + project_id)


def manage_project(request, project_id):
    return render_to_response('ManageProject.html', context_instance=RequestContext(request))


def projects(request):
    args = {}
    args.update(csrf(request))
    projects = Project.objects.all()
    #print("XXX", projects[0])
    # projects = [Project()]
    #print(projects)

    # print(Project.objects.all())
    args.update({"projects": projects})
    return render_to_response('Projects.html', args, context_instance=RequestContext(request))


def logout(request):
    print("!!!", request.user)

    if request.user.is_authenticated():
        auth.logout(request)
    return redirect('/index')


def about(request):
    return render_to_response('About.html', context_instance=RequestContext(request))


def profile(request, user_id):
    user = User.objects.filter(id=user_id)[0]
    args = {'user_cur': user, 'user_id': request.user.id}
    return render_to_response('Profile.html', args, context_instance=RequestContext(request))


def profile_edit(request, user_id):
    user = User.objects.filter(id=user_id)[0]
    args = {'user': user}
    args.update(csrf(request))
    return render_to_response('EditProfile.html', args, context_instance=RequestContext(request))


def profile_apply_changes(request, user_id):
    username = request.POST.get('username', '')
    email = request.POST.get('email', '')
    phone = request.POST.get('phone', '')
    description = request.POST.get('description', '')
    country = request.POST.get('country', '')

    user = User.objects.filter(id=user_id)[0]

    user.username = username
    user.email = email

    userinfo = UserInfo.objects.filter(user=user)[0]

    userinfo.phone = phone
    userinfo.description = description
    userinfo.country = country

    # user.userinfo.phone = phone
    # user.userinfo.description = description
    # user.userinfo.country = country

    user.save()
    userinfo.save()

    return redirect('/index/profile/{}/'.format(user_id))


def users(request):
    users = User.objects.all()
    args = {'users': users}
    return render_to_response('Users.html', args, context_instance=RequestContext(request))
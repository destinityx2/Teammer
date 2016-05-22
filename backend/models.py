    # This file is part of Teammer.

    # Teammer is free software: you can redistribute it and/or modify
    # it under the terms of the GNU General Public License as published by
    # the Free Software Foundation, version 3.

    # Teammer is distributed in the hope that it will be useful,
    # but WITHOUT ANY WARRANTY; without even the implied warranty of
    # MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    # GNU General Public License for more details.

    # You should have received a copy of the GNU General Public License
    # along with Teammer.  If not, see <http://www.gnu.org/licenses/>.

from django.db import models
from django.contrib.auth.models import User


class UserInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=1000, default='')
    phone = models.CharField(max_length=15, default='')
    country = models.CharField(max_length=20, default='')
    photo = models.URLField(default='img/user_default.png')


class Project(models.Model):
    project_name = models.CharField(max_length=250, default='')
    description = models.CharField(max_length=2000, default='')
    skills = models.CharField(max_length=2000, default='')
    creator = models.ForeignKey(User)
    publication_date = models.DateField(auto_now_add=True)
    max_people = models.IntegerField()


class ProjectUsers(models.Model):
    user = models.ForeignKey(User)
    project = models.ForeignKey(Project)
    start_date = models.DateField(auto_now_add=True)


class Applicants(models.Model):
    user = models.ForeignKey(User)
    project = models.ForeignKey(Project)
    application_date = models.DateField(auto_now_add=True)
    accepted = models.BooleanField(default=False)
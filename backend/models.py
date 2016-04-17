from django.db import models
from django.contrib.auth.models import User


class UserInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=1000, default='')
    phone = models.CharField(max_length=15, default='')
    country = models.CharField(max_length=20, default='')


class Project(models.Model):
    description = models.CharField(max_length=250, default='')
    skills = models.CharField(max_length=30, default='')
    creator = models.ForeignKey(User)
    publication_date = models.DateField(auto_now_add=True)
    max_people = models.IntegerField()


class ProjectUsers(models.Model):
    user = models.OneToOneField(User)
    project = models.OneToOneField(Project)
    start_date = models.DateField(auto_now_add=True)

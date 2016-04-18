from django.contrib import auth
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render_to_response, redirect
from django.template.context_processors import csrf
from django.template.loader import get_template

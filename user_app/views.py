from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render

from .models import Person

from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.views.generic import TemplateView
from django.views.generic import FormView, UpdateView

# from .forms import SignUpForm, ProfileForm
from .models import Profile


# def index(request):
#     return render(request, 'index.html')


class Index(TemplateView):
    template_name = 'index.html'


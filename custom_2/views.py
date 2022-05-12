# пример 2: Расширенный профиль пользователя
from django import forms
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.views.generic import FormView, UpdateView, TemplateView

from user_app.models import Profile
from .forms import SignUpForm, ProfileForm


class CreateUser(FormView):
    # pass
    form_class = SignUpForm
    template_name = 'signup2.html'
    success_url = '/'

    def form_valid(self, form):
        user = form.save()
        user.refresh_from_db()
        user.profile.first_name = form.cleaned_data.get('first_name')
        user.profile.last_name = form.cleaned_data.get('last_name')
        user.profile.email = form.cleaned_data.get('email')
        user.save()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        login(self.request, user)
        return super(CreateUser, self).form_valid(form)


class UpdateProfile(UpdateView):
    model = Profile
    form_class = ProfileForm
    template_name = 'user_profile.html'
    success_url = '/'

    def form_valid(self, form):
        user = self.request.user
        user.profile.phone = form.cleaned_data.get('phone')
        user.profile.birthday = form.cleaned_data.get('birthday')
        # если в request есть photo, добавляем его в профиль
        if 'photo' in self.request.FILES:
            print('found it')
            user.profile.photo = self.request.FILES['photo']

        print(self.request.FILES)
        print(user.profile.photo)
        user.save()
        return super(UpdateProfile, self).form_valid(form)


class AllUsers(TemplateView):
    template_name = "all_users.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['users'] = User.objects.all()
        return context

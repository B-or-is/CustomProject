# пример 3: наследование от AbstractBaseUser для реализации аутентификации по e-mail вместо username (см.models.py)
# не проверялся, т.к. необходимо делать миграции, которые могли нарушить структуру БД из предыдущих примеров.
# from django.contrib.auth import login, authenticate
# from .forms import RegisterForm
# from django.views.generic import TemplateView
# from django.views.generic import FormView
# from .models import User
#
#
# class Index(TemplateView):
#     template_name = 'index.html'
#
#
# class CreateUser(FormView):
#     form_class = RegisterForm
#     template_name = 'signup.html'
#     success_url = '/'
#
#     def form_valid(self, form):
#         user = form.save()
#         authenticate(username=user.email, password=user.password)
#         login(self.request, user)
#         return super(CreateUser, self).form_valid(form)
#
#
# class AllUsers(TemplateView):
#     template_name = "all_users.html"
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#
#         context['users'] = User.objects.all()
#         return context

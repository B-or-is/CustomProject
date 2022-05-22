from django.db import models
from django.core.mail import send_mail
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import AbstractBaseUser
# from django.utils.translation import ugettext_lazy as _   # устарело
from django.utils.translation import gettext_lazy as _      # начиная с версии 4

# from .managers import UserManager
from custom_3.managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    # дополнительные поля для модели пользователя
    email = models.EmailField(_('email'), unique=True)      # уникальное, т.к. используется вместо username
    first_name = models.CharField(_('name'), max_length=30, blank=True)
    last_name = models.CharField(_('surname'), max_length=30, blank=True)
    date_joined = models.DateTimeField(_('registered'), auto_now_add=True)
    is_active = models.BooleanField(_('is_active'), default=True)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)

    objects = UserManager()     # используем свой менеджер (см.managers.py)

    USERNAME_FIELD = 'email'    # указываем поле, используемое вместо username
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def get_full_name(self):
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        send_mail(subject, message, from_email, [self.email], **kwargs)

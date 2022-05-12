from django.db import models

from django.contrib.auth.models import User
from user_app.managers import PersonManager

from django.db.models.signals import post_save
from django.dispatch import receiver
from phone_field import PhoneField


# пример 1: Создание proxy
class Person(User):                 # модель, наследуемая от модели пользователя
    people = PersonManager()        # добавлен кастомный менеджер

    class Meta:
        proxy = True                # для написания модели как proxy
        ordering = ('first_name',)  # указываем, по какому полю будет сортировка

    def do_something(self):         # в User данного метода нет (для изменения модели пользователя)
        print(self.username)


# пример 2: Расширенный профиль пользователя (модель профиля связана с моделью User через ключевое поле)
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)         # связь 1 к 1 на модель пользователя
    phone = PhoneField(blank=True, help_text='Contact phone number')    # реализовано библиотекой django-phone-field
    birthday = models.DateField(blank=True, null=True)
    email = models.EmailField(max_length=150)
    photo = models.ImageField(upload_to='profile_pics')                 # картинка
    bio = models.TextField()                                            # текстовое поле (описание)

    def __str__(self):
        return self.user.username                                       # для просмотра имени вместо ячейки памяти


# когда создается новый пользователь, создается инстанс модели User,
# отправляется сигнал, который приходит в данную функцию и обрабатывается
@receiver(post_save, sender=User)
def update_profile_signal(sender, instance, created, **kwargs):
    # если флажок created установлен, создается объект Profile, в который добавляем поле user и сохраняем его
    if created:
        Profile.objects.create(user=instance)
        instance.profile.save()
